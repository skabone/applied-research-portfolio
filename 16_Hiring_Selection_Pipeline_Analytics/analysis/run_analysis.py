from __future__ import annotations

import csv
import argparse
import sqlite3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
SQL_DIR = ROOT / "sql"
DOCS_DIR = ROOT / "docs"
OUT_DIR = ROOT / "analysis" / "outputs"


def _read_sql(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _load_csv_to_table(conn: sqlite3.Connection, csv_path: Path, table: str) -> None:
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        placeholders = ",".join("?" for _ in header)
        insert_sql = f"INSERT INTO {table} ({','.join(header)}) VALUES ({placeholders})"
        conn.executemany(insert_sql, reader)


def _query_to_rows(conn: sqlite3.Connection, sql: str) -> tuple[list[str], list[tuple[object, ...]]]:
    cur = conn.execute(sql)
    cols = [d[0] for d in cur.description]
    rows = cur.fetchall()
    return cols, rows


def _write_csv(path: Path, cols: list[str], rows: list[tuple[object, ...]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        w.writerows(rows)


def _md_table(cols: list[str], rows: list[tuple[object, ...]], max_rows: int = 25) -> str:
    # Minimal markdown table renderer (keeps dependencies at stdlib only)
    shown = rows[:max_rows]
    lines = []
    lines.append("| " + " | ".join(str(c) for c in cols) + " |")
    lines.append("|" + "|".join(["---"] * len(cols)) + "|")
    for r in shown:
        lines.append("| " + " | ".join("" if v is None else str(v) for v in r) + " |")
    if len(rows) > max_rows:
        lines.append(f"\n_({len(rows) - max_rows} more rows not shown)_")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run SQL-first analysis on synthetic hiring pipeline data.")
    parser.add_argument(
        "--keep-db",
        action="store_true",
        help="Write a SQLite database file to analysis/outputs/ (otherwise uses an in-memory DB).",
    )
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    db_path = OUT_DIR / "pipeline.sqlite"
    if args.keep_db and db_path.exists():
        db_path.unlink()

    conn = sqlite3.connect(str(db_path) if args.keep_db else ":memory:")
    try:
        conn.executescript(_read_sql(SQL_DIR / "01_schema.sql"))

        _load_csv_to_table(conn, DATA_DIR / "candidates.csv", "candidates")
        _load_csv_to_table(conn, DATA_DIR / "assessments.csv", "assessments")
        _load_csv_to_table(conn, DATA_DIR / "pipeline_events.csv", "pipeline_events")
        _load_csv_to_table(conn, DATA_DIR / "outcomes.csv", "outcomes")
        conn.commit()

        funnel_cols, funnel_rows = _query_to_rows(conn, _read_sql(SQL_DIR / "02_funnel_metrics.sql"))
        _write_csv(OUT_DIR / "funnel_metrics.csv", funnel_cols, funnel_rows)

        subgroup_cols, subgroup_rows = _query_to_rows(
            conn, _read_sql(SQL_DIR / "03_subgroup_selection_ratios.sql")
        )
        _write_csv(OUT_DIR / "subgroup_selection_ratios.csv", subgroup_cols, subgroup_rows)

        ai_cols, ai_rows = _query_to_rows(conn, _read_sql(SQL_DIR / "04_adverse_impact_screen.sql"))
        _write_csv(OUT_DIR / "adverse_impact_screen.csv", ai_cols, ai_rows)

        flagged = [r for r in ai_rows if int(r[7]) == 1]  # flagged_under_4_5ths column

        lines: list[str] = [
            "# Hiring & Selection Pipeline — Results Snapshot (Synthetic Data)",
            "",
            "This snapshot is generated from the synthetic datasets in `data/` and SQL queries in `sql/`.",
            "",
            "## Funnel counts by stage",
            "",
            _md_table(funnel_cols, funnel_rows, max_rows=10),
            "",
            "## Adverse impact screen (4/5ths rule) — flagged rows",
            "",
        ]

        if flagged:
            lines.append(_md_table(ai_cols, flagged, max_rows=30))
        else:
            lines.append("_No rows flagged under the 4/5ths rule in this synthetic run._")

        lines += [
            "",
            "## Notes / limitations",
            "",
            "- This is a **screening** workflow for interpretation and documentation practice, not a legal conclusion.",
            "- The synthetic generator intentionally introduces small subgroup shifts to demonstrate how to detect and discuss potential impact.",
            "- In real work, you would add minimum-n thresholds, job-relatedness evidence, and a validation plan before changing selection decisions.",
            "",
        ]

        (DOCS_DIR / "Results_Snapshot.md").write_text("\n".join(lines), encoding="utf-8")
        print("Wrote:", DOCS_DIR / "Results_Snapshot.md")
        print("Wrote outputs to:", OUT_DIR)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
