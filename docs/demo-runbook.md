# Demonstration and evidence runbook

This runbook describes future validation after final source recovery. It is not a log of tests performed for this public release. The only executable tests currently included are synthetic unit tests for the recovered KPI helper.

## Preparation

Use an isolated, authorized lab. Record the commit, component versions, image digests, network-policy implementation and active allow rules. Synchronize clocks. Keep raw events and captures outside this repository until separately sanitized.

Recover the actual `/webhook/alert` schema from final source before generating payloads; do not substitute the guide's `/falco-webhook` interface.

## Scenario 1: low-risk alert

Submit a schema-valid synthetic event with a controlled lab identity. Capture the received event, score, correlation key and decision. Verify that low-risk activity does not trigger blocking. Confirm that the same input and configuration yield the expected score.

## Scenario 2: repeated critical activity

Generate repeated authorized test events within and outside the configured correlation window. Observe score changes, duplicate handling and alert-to-incident grouping. Verify exclusions and exercise malformed/replayed inputs before enabling automatic response.

## Scenario 3: containment and recovery

Use a disposable target. Observe the response decision and action result, then independently test network reachability from controlled endpoints in both directions. Capture the full effective policy set. A created firewall rule or NetworkPolicy is insufficient evidence on its own.

Validate the actual incident lifecycle and the recovery action after analyst authorization. Verify restored connectivity and audit records, including failure and retry paths.

## Scenario 4: delivery controls

Use non-secret scanner fixtures and a controlled vulnerable test dependency. Record each job's status and the final pipeline outcome. Check that critical policy failures prevent promotion. Separately test unsigned-image rejection at admission; do not infer it from a successful signing job.

## Measurement contract

Record distinct UTC timestamps for attack start, alert generation, SOAR receipt, scoring completion, response start, action completion and independently verified containment. Document the exact intervals used for every metric.

The recovered KPI helper expects `t_attack`, `t_alert` and `t_remediation` fields. Define `t_alert` consistently before using it: alert generation and SOAR receipt are different boundaries. Do not pool unlike intervals or label ingestion latency as full MTTD.

Publish sample counts per metric, missing/failed samples, repeated trials, median and tail behavior, and false positives. Preserve a sanitized dataset before claiming reproducible results. The synthetic unit-test fixture is not measurement evidence.
