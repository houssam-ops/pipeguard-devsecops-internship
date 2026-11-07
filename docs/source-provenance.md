# Source provenance

PipeGuard is the public portfolio name chosen by the project owner. This repository was prepared from a private academic report and a separately supplied execution guide. Neither original document is distributed. The report was used as a private reference for the README; no report pages or screenshots were extracted into this repository.

## Recovered guide artifacts

These files come from actual fenced code blocks in the execution guide, not from an invented reconstruction of the final deployment:

- `examples/ansible/hardening.yml`: week 4 hardening playbook; original operational content retained.
- `examples/kubernetes/default-deny-all.yaml`: week 6 ingress/egress default-deny policy; original operational content retained.
- `examples/detection/falco-shell-rule.yaml`: week 12 shell-process detection rule; original operational content retained.
- `examples/detection/wazuh-sca.xml`: week 13 SCA configuration excerpt; original operational content retained.
- `examples/pipelines/security-scans.gitlab-ci.yml.example`: week 9 scan-stage excerpt; the registry address placeholder is replaced by a reserved `.invalid` hostname.
- `examples/soar/soar-responder.py.example`: section 6.1 responder prototype, retained as inert review material. It is incomplete and unsafe to expose as a service without changes. The commented CTI integration is a stub, not implemented functionality.
- `metrics/compute_kpi.py`: week 15 KPI helper; calculation behavior is preserved. It exposes functions and has no command-line entry point.

Headers identifying provenance were added. French comments in historical excerpts are retained where they explain the supplied code. Instructions or aspirations within those comments are historical context, not evidence that the features were delivered.

## Newly authored for this public release

The English README and documentation, `.gitignore`, `.editorconfig`, security policy, synthetic unit tests, publication validator and GitHub repository-check workflow were created during portfolio preparation. They are supporting publication work, not original PFA implementation claims.

## Missing artifacts

The final SOAR source and blocking/unblocking scripts, systemd unit, dependency locks, complete Ansible roles/inventory, production-shaped manifests, actual CI configuration, deployed Kyverno policies, Wazuh integrations/decoders, Vault configuration and sanitized raw KPI data were not supplied. Neither dashboard source nor export files nor a demonstration video were supplied.

No application source, configuration or measurement is reconstructed from a screenshot and presented as an original file. The supplied guide's whole text is not copied into this repository because it mixes planning requirements, historical status and private context.
