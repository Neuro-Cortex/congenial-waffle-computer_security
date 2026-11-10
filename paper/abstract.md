# Abstract (working draft)

Large language models (LLMs) are expected to follow safety policies while remaining useful on benign tasks. However, output-level evaluations alone provide limited insight into the internal representations that support refusal and policy-compliant behavior. Recent interpretability and representation-steering methods offer tools for examining and intervening on model activations, but identifying a feature that correlates with safety behavior does not establish that the feature causally controls that behavior.

This project proposes an interpretability-led framework for studying internal safety features in LLMs. The workflow combines sparse feature discovery, candidate-feature interpretation, causal validation through controlled activation interventions, and targeted steering. Evaluation is designed to measure both safety behavior under adversarial prompting and utility on benign tasks, including over-refusal, response quality, and capability changes. The study will document model and dataset provenance, intervention controls, uncertainty, and limitations to support reproducibility.

The work is currently a research plan. The abstract must be revised after experiments are completed; no empirical improvement is claimed at this stage.

**Keywords:** large language models, mechanistic interpretability, sparse autoencoders, safety features, causal intervention, activation steering, jailbreak robustness.
