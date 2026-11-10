# Literature review matrix

This is a starter reading list, not a completed systematic review. Verify metadata, versions, and claims against the publisher / author copy before citing in the final manuscript.

| Area | Work | Why it matters | Notes to extract |
|---|---|---|---|
| Sparse features | Bricken et al., *Towards Monosemanticity: Decomposing Language Models With Dictionary Learning* (2023) | Early SAE-based feature discovery in language models | Feature interpretability, scaling, limitations |
| Sparse features | Cunningham et al., *Sparse Autoencoders Find Highly Interpretable Features in Language Models* (2023) | SAE feature interpretability | Training setup, evaluation, caveats |
| Causal feature circuits | Marks et al., *Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models* (2025) | Feature-level causal graphs and interventions | Causal metrics, faithfulness, completeness |
| Representation steering | Zou et al., *Representation Engineering: A Top-Down Approach to AI Transparency* (2023) | Representation-level control and analysis | Representation extraction and steering |
| Activation steering | Turner et al., *Activation Addition: Steering Language Models Without Optimization* (2023) | Activation-based steering | Steering vector construction and side effects |
| Refusal mechanisms | Arditi et al., *Refusal in Language Models Is Mediated by a Single Direction* (2024) | Internal direction associated with refusal | Scope, generalization, causal evidence |
| Jailbreak evaluation | Wei et al., *Jailbroken: How Does LLM Safety Training Fail?* (2023) | Taxonomy / evaluation of safety failures | Threat model and failure categories |
| Steering safety | Rimsky et al., *Steering Llama 2 via Contrastive Activation Addition* (2024) | Contrastive activation steering | Safety behavior and utility trade-offs |

## Review questions
1. What is the unit of analysis: neuron, direction, SAE feature, or circuit?
2. What evidence supports interpretability?
3. What evidence supports causal relevance?
4. What intervention is applied and what controls are used?
5. How are safety and benign utility evaluated?
6. What failure modes and limitations are acknowledged?
7. Which findings replicate across models, layers, and prompt distributions?

## Citation policy
Use the original paper or official proceedings page as the source. Do not rely on search snippets for bibliographic metadata. Add DOI / stable URL and access date to `paper/references.bib` after verification.
