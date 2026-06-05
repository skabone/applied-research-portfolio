"""Compatibility wrapper for the standard project source file."""

from pathlib import Path
import runpy


runpy.run_path(str(Path(__file__).with_name("04_Source_Code.py")), run_name="__main__")
