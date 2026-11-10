# Experiments

This directory contains reproducibility scaffolding. It does not include model weights, benchmark data, jailbreak payloads, or a ready-made steering implementation.

## Suggested run order
1. Freeze evaluation-set version and model checkpoint.
2. Run `python scripts/validate_results.py --input results/example_metrics.csv` on a copy of the example schema.
3. Implement model-specific activation collection in a separate module.
4. Save every run configuration and raw metric output.
5. Keep final evaluation prompts held out from feature selection and steering-parameter tuning.

See `../research/methodology.md` before implementing experiments.
