# Screenshot provenance

The owner explicitly requested screenshots from the internship report in the README. These three embedded images were extracted with Poppler `pdfimages`, visually inspected at original resolution and checked with OCR. They were selected because they contain no visible credentials, personal names, email addresses, private network addresses or secret URLs. Their pixels were not edited, redrawn or generated. Only these images are published, not PDF pages or the PDF document.

Generic interface identities such as “Administrator”, the product name “wazuh”, aggregate test-event counters and historical pipeline identifiers remain visible. These reflect the original screenshots. No claim is made that a warning state is a passing pipeline or that dashboard navigation tiles prove integration completeness.

## gitlab-security-pipeline.png

- Source: Figure 5.34 (PDF page 86).
- Content: GitLab pipeline stages; the original warning and failed-job count remain visible.
- SHA-256: `f80f1cd986b8a360075cd5567b1854e2a4bb554876d79ad3f35c200a2aa360ad`

## wazuh-security-overview.png

- Source: Figure 6.1 (PDF page 89).
- Content: Wazuh overview with aggregate alert counts and navigation modules.
- SHA-256: `49914628fd0ee6074f16f7128a3fa6ee021923ca90c83d3af53ab8695fb3cf2a`

## wazuh-threat-hunting.png

- Source: Figure 6.3 (PDF page 90).
- Content: Wazuh Threat Hunting view with aggregate activity and MITRE ATT&CK labels.
- SHA-256: `834a1220727cbc7a256bfa95a7c424f8f6136d380202a8b867cdab053282c397`

## Maintenance

The publication validator pins these exact image bytes. Before changing a screenshot, inspect the full-resolution image, OCR all visible text, inspect metadata and update the approval checksum only after review. Secret scanners do not reliably inspect text embedded in images. Other screenshots from the private report were not approved for publication.
