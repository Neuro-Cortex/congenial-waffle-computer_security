# Understanding and Steering Internal Safety Features in Large Language Models

[![Research](https://img.shields.io/badge/type-academic%20research-2563eb)]()
[![Status](https://img.shields.io/badge/status-proposal%20%2F%20in%20progress-orange)]()
[![Visibility](https://img.shields.io/badge/repository-private-6b7280)]()
[![License](https://img.shields.io/badge/license-see%20LICENSE-lightgrey)]()

> A research workspace for investigating how safety-related representations are encoded inside large language models (LLMs), how their causal roles can be tested, and whether targeted interventions can improve resistance to jailbreaks while preserving helpfulness on benign requests.

**Program:** synthesis_E6  
**Repository:** `computer-security-research`  
**Research status:** Planning / literature review. No experimental findings are claimed in this repository unless explicitly recorded in `results/`.

## Research team

- Pollob Das


Update affiliations, student IDs, and contribution roles only after confirming the details that should be made public. This repository is intended to remain private.

## 1. Research overview

LLM safety behavior is often evaluated from model outputs, but output-only evaluation does not fully explain which internal representations contribute to refusal, policy compliance, or resistance to adversarial prompting. This project studies an interpretability-led workflow:

1. **Discover candidate safety features** using sparse autoencoders (SAEs) or other validated representation-analysis methods.
2. **Validate causal relevance** using controlled interventions such as activation patching, ablation, and feature-level steering.
3. **Evaluate safety and utility jointly** on harmful/adversarial and benign prompt sets.
4. **Measure side effects** including over-refusal, capability degradation, fluency changes, and distribution sensitivity.

The central research question is:

> Can interpretable, causally validated internal features be used to steer LLM safety behavior more selectively, improving robustness to jailbreak-style prompts without materially degrading benign task performance?

This is a research question, not an established result. The repository separates hypotheses, methods, and measured findings.

## 2. Research gap and motivation

Prior work has developed methods for discovering interpretable features and methods for steering model representations. A remaining challenge is to connect these stages in a rigorous safety evaluation: a feature that correlates with refusal is not necessarily causally responsible for it, and changing a feature may alter unrelated capabilities.

This project therefore emphasizes:
- the distinction between correlation and causal evidence;
- feature-level rather than only neuron- or layer-level analysis;
- controlled baselines and intervention controls;
- both adversarial robustness and benign-task utility;
- transparent reporting of negative results and limitations.

## 3. Objectives

- Review methods for feature discovery, representation analysis, and activation steering.
- Define an auditable protocol for identifying candidate safety-related features.
- Test candidate features with causal interventions and matched controls.
- Evaluate refusal behavior under a documented, non-operational jailbreak benchmark.
- Quantify over-refusal and benign capability changes.
- Document reproducible configurations, evaluation data provenance, and limitations.

## 4. Proposed workflow

```text
Model + documented evaluation prompts
                 |
                 v
      Baseline behavior evaluation
                 |
                 v
   Activation collection / instrumentation
                 |
                 v
      SAE or feature discovery
                 |
                 v
 Candidate feature interpretation
                 |
                 v
 Causal tests: ablation / patching / controls
                 |
                 v
   Targeted steering experiments
                 |
                 v
 Safety + helpfulness + side-effect metrics
                 |
                 v
       Analysis and reporting
```

## 5. Repository map

```text
paper/             manuscript, abstract, and bibliography
research/          research question, hypotheses, literature review, methodology
experiments/       reproducible experiment plans and code
datasets/          dataset cards and data acquisition notes (no unlicensed data)
results/           empty until verified measurements are produced
figures/           publication-ready figures and source data
presentation/      slides and speaker notes
docs/              ethics, reproducibility, contribution, and project decisions
.github/           issue templates and pull-request template
```

## 6. Getting started

### Requirements

- Python 3.10+
- Git
- A compatible model/SAE checkpoint and the relevant framework, if experiments require them
- GPU access may be required for model-scale experiments

### Setup

```bash
git clone <private-repository-url>
cd computer-security-research

python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r experiments/requirements.txt
```

### Current code status

The included Python files are **analysis scaffolds**, not a complete SAE implementation or a validated safety intervention. They provide a clean place to record metrics and compare experimental conditions. Add model-specific hooks only after selecting and documenting the model, layer, SAE, and evaluation protocol.

## 7. Evaluation plan

Report results separately for:
- refusal / policy-compliance behavior on the approved safety evaluation set;
- jailbreak robustness under the benchmark's documented threat model;
- benign task accuracy or task-specific quality;
- over-refusal rate on benign prompts;
- fluency and response-quality measures;
- intervention magnitude and stability across random seeds / prompt variants.

Do not combine these into a single score without explaining normalization and weighting. Report confidence intervals or uncertainty estimates where appropriate.

## 8. Research integrity

- Never present planned experiments as completed experiments.
- Never fabricate citations, metrics, model behavior, or benchmark results.
- Record model identifiers, checkpoint hashes, software versions, seeds, and prompt-set versions.
- Respect dataset licenses, model terms, privacy, and institutional review requirements.
- Do not publish sensitive prompts, credentials, private datasets, or personally identifiable information.
- Keep harmful-prompt examples abstract or redacted where reproducing them would create operational risk.

## 9. Current status and next milestones

- [x] Define repository structure and research scope
- [x] Draft research question and objectives
- [x] Add methodology and evaluation templates
- [ ] Confirm target model(s), layers, and SAE checkpoint(s)
- [ ] Complete source-verified literature review
- [ ] Finalize dataset / benchmark protocol
- [ ] Run baseline evaluation
- [ ] Run causal validation experiments
- [ ] Run steering experiments and utility checks
- [ ] Analyze results and write the manuscript

## 10. Citation

When citing this repository in a report, use the actual author list, institution, and year after they are confirmed. Do not cite this scaffold as evidence of experimental findings.
