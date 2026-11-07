"""Publication guard for tracked files; supplements manual review and Gitleaks.

New portfolio tooling, not part of the original environment implementation.
Only reports filenames/reasons, never the content of a possible credential.
"""
from pathlib import Path
import ast
import hashlib
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
APPROVED_SCREENSHOTS = {'assets/screenshots/gitlab-security-pipeline.png': 'f80f1cd986b8a360075cd5567b1854e2a4bb554876d79ad3f35c200a2aa360ad',
 'assets/screenshots/wazuh-security-overview.png': '49914628fd0ee6074f16f7128a3fa6ee021923ca90c83d3af53ab8695fb3cf2a',
 'assets/screenshots/wazuh-threat-hunting.png': '834a1220727cbc7a256bfa95a7c424f8f6136d380202a8b867cdab053282c397'}
SAFE_SPECIAL = {'.gitignore', '.editorconfig'}
SAFE_SUFFIXES = {'.md', '.py', '.yaml', '.yml', '.xml', '.example'}
SECRET_PATTERNS = {
    'private key': re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    'GitHub credential': re.compile(r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,})'),
    'GitLab credential': re.compile(r'\bglpat-[A-Za-z0-9_-]{16,}'),
    'Slack webhook': re.compile(r'https://hooks\.slack\.com/services/[A-Za-z0-9/]{20,}'),
    'Vault token': re.compile(r'\bhv[sb]\.[A-Za-z0-9_-]{20,}'),
    'private infrastructure address': re.compile(r'\b(?:10\.(?:\d{1,3}\.){2}\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})\b'),
}


def main():
    try:
        result = subprocess.run(
            ['git', 'ls-files', '-z'], cwd=ROOT, check=True, capture_output=True,
        )
    except (OSError, subprocess.CalledProcessError):
        print('Run inside the initialized repository after staging its intended files.')
        return 1
    names = result.stdout.decode().split('\0')
    failures = []
    checked = 0
    for name in filter(None, names):
        path = ROOT / name
        checked += 1
        if path.is_symlink():
            failures.append((name, 'symlinks are not allowed in the publication set'))
            continue
        if name in APPROVED_SCREENSHOTS:
            image_bytes = path.read_bytes()
            if (not image_bytes.startswith(b'\x89PNG\r\n\x1a\n')
                    or hashlib.sha256(image_bytes).hexdigest() != APPROVED_SCREENSHOTS[name]):
                failures.append((name, 'image differs from visually and OCR-reviewed original'))
            continue
        if path.name not in SAFE_SPECIAL and path.suffix not in SAFE_SUFFIXES:
            failures.append((name, 'file type outside the reviewed publication set'))
            continue
        if path.stat().st_size > 250_000:
            failures.append((name, 'unexpectedly large file'))
            continue
        try:
            source = path.read_text(encoding='utf-8')
        except UnicodeError:
            failures.append((name, 'non-UTF-8 content'))
            continue
        if '\x00' in source or source.startswith('%PDF-'):
            failures.append((name, 'binary or PDF content'))
        for reason, pattern in SECRET_PATTERNS.items():
            if pattern.search(source):
                failures.append((name, reason))
        if path.suffix == '.py' or path.name.endswith('.py.example'):
            try:
                ast.parse(source, filename=name)
            except SyntaxError:
                failures.append((name, 'Python syntax error'))
        if path.suffix == '.md':
            # Validate local Markdown links; anchors and web links are not filesystem paths.
            for target in re.findall(r'!?\[[^\]]+\]\(([^)]+)\)', source):
                if '://' in target or target.startswith('#'):
                    continue
                destination = (path.parent / target.split('#', 1)[0]).resolve()
                if not destination.is_relative_to(ROOT) or not destination.exists():
                    failures.append((name, 'missing or out-of-tree documentation link'))
    if checked == 0:
        failures.append(('.', 'no tracked files to check'))
    for name, reason in failures:
        print(f'FAIL {name}: {reason}')
    if failures:
        return 1
    print(f'PASS: {checked} tracked files; publication boundaries, image checksums, links and Python syntax checked.')
    print('Manual review and a full-history secret scan remain required.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
