# Methodology (protocol draft)

## Phase 1 — Model and environment selection
Record model name, exact checkpoint/revision, tokenizer, framework versions, hardware, context length, and access conditions. Select a model only when its terms permit the intended research.

## Phase 2 — Evaluation-set design
Create documented benign and safety evaluation partitions. Use established, licensed benchmarks where possible. Record source, version, license, inclusion criteria, exclusions, language coverage, and known limitations. Keep sensitive examples access-controlled.

## Phase 3 — Baseline evaluation
Run the unmodified model on the fixed evaluation set. Save raw outputs securely, prompt IDs, configuration, random seeds, and scoring decisions. Establish baseline refusal, over-refusal, task-quality, and stability measures.

## Phase 4 — Feature discovery
Capture activations at documented layers and token positions. Apply a documented SAE or other feature-analysis method. Record SAE checkpoint, dictionary size, sparsity settings, activation normalization, and reconstruction metrics. Candidate features must be selected using a predeclared procedure where feasible.

## Phase 5 — Interpretation
Inspect top-activating examples and counterexamples. Use multiple prompt contexts and independent reviewers when possible. Avoid naming a feature based on a single example. Record ambiguity and polysemantic behavior.

## Phase 6 — Causal validation
Use controlled ablation, activation patching, or other justified interventions. Include sham / random-feature controls, matched prompts, and intervention-strength sweeps. A causal claim requires evidence that the intervention changes the target behavior under the stated assumptions; correlation or a feature label alone is insufficient.

## Phase 7 — Targeted steering
Define intervention direction, magnitude, location, and duration before evaluation. Compare against baseline and appropriate non-targeted controls. Avoid tuning on the held-out evaluation set.

## Phase 8 — Evaluation and analysis
Report safety and utility metrics separately, uncertainty estimates, subgroup / prompt-category analyses where justified, and all material deviations from the protocol.

## Reproducibility record
For each run, save:
- run ID and UTC timestamp;
- model / tokenizer / SAE identifiers and hashes;
- code commit hash and package versions;
- dataset version and prompt IDs;
- intervention configuration and random seed;
- metric definitions and scoring version;
- output artifact locations and access classification.
