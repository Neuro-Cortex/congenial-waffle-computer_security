# Manuscript outline

1. **Introduction**
   - LLM safety and the limits of output-only evaluation
   - Internal representations as an object of study
   - Research question and contributions

2. **Background and related work**
   - Mechanistic interpretability
   - Sparse autoencoders and feature dictionaries
   - Representation engineering and activation steering
   - Refusal mechanisms and jailbreak evaluation

3. **Research gap**
   - Feature discovery does not itself prove causal relevance
   - Steering can create collateral changes
   - Safety and benign utility must be evaluated together

4. **Research questions and hypotheses**
   - RQ1: Can candidate safety-related features be identified consistently?
   - RQ2: Which candidates show causal effects under controlled interventions?
   - RQ3: Can targeted steering change safety behavior with limited benign-task degradation?
   - H1 (to test): Some candidate features will show measurable causal influence on refusal-related behavior.
   - H2 (to test): More selective interventions will produce a better safety/utility trade-off than broad activation changes.
   - Hypotheses are provisional and must not be written as findings.

5. **Methodology**
   - Model and checkpoint selection
   - Prompt-set construction and governance
   - Activation capture and SAE feature discovery
   - Feature interpretation and candidate selection
   - Causal tests and intervention controls
   - Steering protocol

6. **Evaluation**
   - Safety / refusal metrics
   - Adversarial robustness
   - Benign utility and over-refusal
   - Fluency and stability
   - Statistical analysis

7. **Results**
   - Populate only after experiments; include negative and null results.

8. **Discussion**
   - Interpretation, generalization, limitations, and threats to validity

9. **Conclusion and future work**

10. **References and appendices**
