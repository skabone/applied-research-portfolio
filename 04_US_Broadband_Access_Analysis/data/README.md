# Data

## File

`broadband_access.csv` — county-level public extract, 3,142 raw rows → 3,102
counties after cleaning (see `../04_Source_Code.py`).

## Provenance

A public extract blending two sources:

- **IMLS Indicators Workbook** (primary): county-level broadband and
  socioeconomic indicators compiled by the Institute of Museum and Library
  Services from the American Community Survey 5-year estimates (2014–2018), a
  commercial FCC-linked broadband aggregator (BroadbandNow), and Bureau of Labor
  Statistics local-area unemployment statistics.
- **BroadbandNow Open Data Challenge** (supplementary): publicly released
  county-level broadband infrastructure metrics.

A Simple Maps U.S. counties file supplied latitude/longitude for the Tableau
mapping layer and is not required for the statistics in this project.

## Key columns

| Column | Meaning |
|---|---|
| `home_havebroad%` | Households with home broadband (primary outcome) |
| `poverty_rate%` | County poverty rate |
| `SNAP_recieved%` | Households receiving SNAP |
| `broad_avail` | Formal broadband availability (coverage) |
| `broadProviders_num` | Provider count (IMLS) |
| `broad_cost` | Monthly broadband cost (IMLS) |
| `downave_bbn` | Average download speed (BroadbandNow) |
| `all25_bbn` | 25 Mbps coverage measure (BroadbandNow) |

## Cautions

These are public, multi-source, observational data reflecting roughly the
2014–2018 period. Findings should be read as descriptive patterns for comparison
and targeting, not as causal estimates or current-condition claims. No personal
identifiers are present; the unit of analysis is the county.
