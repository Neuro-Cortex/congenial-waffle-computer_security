# Dataset documentation

Do not commit third-party datasets unless their licenses explicitly permit redistribution. Prefer storing dataset identifiers, version numbers, access instructions, and checksums.

For every dataset, create a dataset card containing:
- name, source, version, and retrieval date;
- license and permitted uses;
- intended task and threat model;
- prompt / sample construction and filtering;
- language and domain coverage;
- sensitive-content handling and access controls;
- known biases, limitations, and contamination risks;
- train / validation / test split policy;
- checksum or immutable version identifier.

Keep private or restricted data outside Git. Never commit credentials, personal data, or raw sensitive prompts.
