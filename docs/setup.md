# Setup and recovery requirements

## Local portfolio checks

Install Git and Python 3.10+; clone this repository and run:

```bash
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -v
```

The helper in `metrics/compute_kpi.py` needs only the Python standard library. No package installation, Kubernetes credentials or cloud account is required for these checks.

## Internship environment reconstruction

This is a reconstruction checklist, not an executable full installer. The exact versions used for the environment are unavailable. Recover versions, image digests, dependency locks and configuration before claiming reproducibility.

1. Prepare three isolated Linux VMs with private administration access. The guide proposes a 16 GB host and 2/4/4 GB VM memory allocation; load-test and resize for the selected software versions.
2. Review the hardening excerpt on a disposable host. Confirm a working non-root SSH session before disabling root access. Recover the missing inventory and complete playbooks.
3. Install K3s from its official documentation, using a restricted kubeconfig and an enforcing network-policy implementation. Record version and configuration.
4. Install GitLab CE, its registry and a Runner. Configure trusted TLS, access controls and a narrowly scoped runner. The pipeline excerpt is an inactive scan-stage example, not a complete build/sign/deploy pipeline.
5. Install and configure Kyverno and Vault; recover admission rules, service accounts and role bindings. Start policy validation in a test namespace and verify intended enforcement before onboarding workloads.
6. Recover the application's real Dockerfile and manifests. Obtain Juice Shop from its official upstream with a pinned release; this repository does not redistribute it or claim that the guide's proposed distroless build works.
7. Add Falco, Wazuh and network telemetry with explicit event schemas and protected transport. The XML/YAML excerpts alone do not establish collection, decoding or integration.
8. Recover the final SOAR service, its dependency lock, service unit and restricted response scripts. Configure authentication, input validation, credentials and exclusions before enabling any response action.
9. Add GitOps deployment and verify sync health, signed-image admission and actual ingress/egress controls. Reconcile all allow policies before claiming containment.
10. Run the demonstration and measurement procedure only after those prerequisites are satisfied.

## Using individual excerpts

`examples/kubernetes/default-deny-all.yaml` targets a namespace named `demo-app`. This is a generic example namespace from the guide, not a disclosed infrastructure identifier. Validate it before any application:

```bash
# Requires a disposable, authorized Kubernetes context and existing demo-app namespace.
kubectl apply --dry-run=server -f examples/kubernetes/default-deny-all.yaml
```

A dry run does not prove traffic isolation. The policy may interrupt services if applied; no apply command is automated here.

`examples/pipelines/security-scans.gitlab-ci.yml.example` is deliberately not named `.gitlab-ci.yml`. Its registry host is reserved and cannot be used as a real deployment target. Adapt and pin scanner versions, reconcile enforcement settings and supply required source directories before activating a reviewed pipeline in GitLab.

The SOAR prototype requires Flask and the Kubernetes Python client, but no tested versions or lockfile were provided. It is retained as review-only source; this release does not install or launch it.

## Official component references

- [K3s documentation](https://docs.k3s.io/)
- [GitLab documentation](https://docs.gitlab.com/)
- [Argo CD documentation](https://argo-cd.readthedocs.io/)
- [Kyverno documentation](https://kyverno.io/docs/)
- [Vault documentation](https://developer.hashicorp.com/vault/docs)
- [Falco documentation](https://falco.org/docs/)
- [Wazuh documentation](https://documentation.wazuh.com/)
- [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/)
