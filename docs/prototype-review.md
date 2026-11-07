# Recovered prototype: technical review

The `.py.example` responder is historical source for inspection. It is not the IP-oriented final service described in the README and must not be started against a live cluster as-is.

## Response and identity

- Its manifest always selects `app: juice-shop` in `demo-app`, even though incoming events supply a namespace and pod name. The policy name does not make the selector pod-specific.
- NetworkPolicies are additive: adding a deny-all policy does not override other policies allowing traffic. The CNI must enforce NetworkPolicy and actual ingress/egress must be tested. See the [Kubernetes NetworkPolicy documentation](https://kubernetes.io/docs/concepts/services-networking/network-policies/).
- The webhook and reversal endpoint lack authentication and authorization. Untrusted alert fields can influence response decisions.
- Repeated policy creation is not idempotent; failure to initialize the Kubernetes client does not stop startup.
- The prototype binds Flask to every interface. No hardened application-server or TLS configuration is supplied.

## Input, correlation and state

- `tags` is treated as a dictionary; common Falco payloads use a list. The deployment-specific event schema is not supplied.
- Incoming severity strings are not fully normalized across Falco's priority vocabulary.
- An in-memory dictionary stores alerts indefinitely; decay changes weights but does not prune state. There is no durable state, replay protection or concurrency strategy.
- Its incident status transitions are partial; the declared lifecycle is not comprehensively enforced.
- CTI returns a stub result. Notification and ticketing are comments rather than integrations.

## Timing

- The response timer starts after correlation, and it ends after policy API creation. It does not confirm data-plane enforcement.
- `kpi_log` does not persist complete attack/response records. The separate KPI helper needs entries that this responder does not produce end-to-end.
- The KPI helper accepts ISO timestamps without validating monotonic order or timezone consistency. Missing samples produce `None`; `n_scenarios` counts all rows, not valid samples for each metric.

## Other recovered excerpts

- The Ansible playbook disables SSH root login but is not comprehensive host hardening. Service naming and SSH configuration precedence must be checked on the selected distribution.
- The GitLab excerpt uses floating image tags and Checkov `--soft-fail`; it cannot support a claim that all scan findings block delivery. Semgrep policy behavior also requires review. Trivy explicitly requests a nonzero exit on selected findings.
- The default-deny policy blocks traffic only within Kubernetes policy semantics and has no necessary application allow rules supplied.
- The Falco rule requires upstream macros and appropriate event/metadata support. Parsing its YAML is not an engine compatibility test.

These observations are a review of the supplied artifacts, not claims that fixes have been deployed. Corrections should be versioned explicitly after final source recovery.
