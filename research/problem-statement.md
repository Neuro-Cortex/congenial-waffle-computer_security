# Problem statement

## Context
LLMs must distinguish requests that should be refused from benign requests that should be answered. Model behavior can be tested through prompts and outputs, but those observations do not directly reveal which internal representations contribute to the behavior.

## Problem
Interpretability methods can identify candidate features associated with concepts or behaviors. However, association is not causation. Intervening on a candidate representation may also alter unrelated capabilities, cause over-refusal, or make model behavior less stable.

## Research question
Can interpretable, causally validated internal features be used to steer LLM safety behavior more selectively, improving robustness to jailbreak-style prompts without materially degrading benign task performance?

## Scope
This project focuses on controlled research evaluation of internal representations and safety-related model behavior. It does not aim to develop jailbreak payloads, bypass deployed safeguards, or provide operational instructions for harmful activity.
