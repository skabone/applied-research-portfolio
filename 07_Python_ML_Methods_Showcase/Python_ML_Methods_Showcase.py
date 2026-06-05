"""Legacy execution wrapper for Project 07.

The current reproducible source lives in `04_Source_Code.py`. This wrapper is
kept so older links to `Python_ML_Methods_Showcase.py` still run the updated
project-local workflow.
"""

from pathlib import Path
import runpy


runpy.run_path(str(Path(__file__).resolve().with_name("04_Source_Code.py")),
               run_name="__main__")
