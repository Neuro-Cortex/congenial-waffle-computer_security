"""Validate a tabular experiment-metrics file.

Expected columns:
run_id, split, metric, value, model_id, dataset_version, seed

This script validates metadata and numeric values; it does not score model outputs.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import pandas as pd

REQUIRED = {
    "run_id", "split", "metric", "value",
    "model_id", "dataset_version", "seed",
}

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to CSV metrics file")
    args = parser.parse_args()

    path = Path(args.input)
    if not path.is_file():
        parser.error(f"File not found: {path}")

    frame = pd.read_csv(path)
    missing = REQUIRED - set(frame.columns)
    if missing:
        parser.error(f"Missing required columns: {', '.join(sorted(missing))}")
    if frame.empty:
        parser.error("Input file has no metric rows.")
    if frame["value"].isna().any():
        parser.error("Metric values contain missing or non-numeric entries.")
    if not pd.api.types.is_numeric_dtype(frame["value"]):
        parser.error("'value' must be numeric.")
    if frame[list(REQUIRED - {"value", "seed"})].isna().any().any():
        parser.error("Required metadata contains missing values.")

    print(f"Validated {len(frame)} rows from {path}")
    print("Reminder: validation checks structure only, not scientific validity.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
