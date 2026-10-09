"""Deterministic checks for the public GitHub profile README.

The central Yolol100/.github github-admin.json owns desired pin order.
No career metrics or project capabilities are inferred by this checker.
"""

import json
import re
import sys
from pathlib import Path

EXPECTED_OWNER = "Yolol100"
EXPECTED_SECTIONS = (
    "Start here",
    "Website & design cases",
    "Selected engineering work",
    "More projects by area",
    "How I work",
    "Background & contact",
)
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
FEATURED_RE = re.compile(
    r"^\|\s*\[[^\]]+\]\(https://github\.com/Yolol100/([A-Za-z0-9_.-]+)\)\s*\|",
    re.MULTILINE,
)
KEY_RE = re.compile(
    r"ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|"
    r"-----BEGIN (?:OPENSSH|RSA|EC) PRIVATE KEY-----"
)


def section_text(readme, title):
    match = re.search(
        rf"^## {re.escape(title)}\s*\n(.*?)(?=^## |\Z)",
        readme,
        flags=re.MULTILINE | re.DOTALL,
    )
    return match.group(1) if match else None


def audit_profile(readme, config):
    errors = []
    if not readme.startswith("# ") or "WordPress" not in readme.splitlines()[0]:
        errors.append("The profile needs a clear WordPress headline")

    headings = re.findall(r"^## (.+?)\s*$", readme, re.MULTILINE)
    if len(headings) != len(set(headings)):
        errors.append("Duplicate section heading")
    for title in EXPECTED_SECTIONS:
        if title not in headings:
            errors.append(f"Missing section: {title}")

    links = LINK_RE.findall(readme)
    targets = [url for _, url in links]
    if not any(url.startswith("https://andrewbaeten.nl/") for url in targets):
        errors.append("Missing portfolio link")
    if not any(url.startswith("https://www.linkedin.com/") for url in targets):
        errors.append("Missing LinkedIn link")
    if not any(url.startswith("mailto:") for url in targets):
        errors.append("Missing email contact")

    cases = section_text(readme, "Website & design cases")
    case_targets = [url for _, url in LINK_RE.findall(cases or "")]
    actual_cases = [
        url for url in case_targets
        if url.startswith("https://andrewbaeten.nl/")
        and not url.rstrip("/").endswith("/category/cases")
    ]
    if len(set(actual_cases)) < 3:
        errors.append("At least three distinct website or plugin cases are required")

    if not isinstance(config, dict) or config.get("owner") != EXPECTED_OWNER:
        errors.append("Invalid central GitHub config owner")
        config = {}
    repositories = config.get("repositories", [])
    names = [
        repo.get("name") for repo in repositories
        if isinstance(repo, dict) and isinstance(repo.get("name"), str)
    ] if isinstance(repositories, list) else []
    if len(names) != len(set(names)) or not names:
        errors.append("Invalid central repository inventory")

    profile = config.get("profile", {})
    pins = profile.get("desired_pins", []) if isinstance(profile, dict) else []
    if not isinstance(pins, list) or len(pins) != 6 or len(set(pins)) != 6:
        errors.append("The central config must define six unique pinned projects")
        pins = []
    if any(pin not in names for pin in pins):
        errors.append("A desired pin is missing from the central inventory")

    selected = section_text(readme, "Selected engineering work")
    selected_repos = FEATURED_RE.findall(selected or "")
    if selected_repos != pins:
        errors.append(f"Selected projects differ from central pin order: {selected_repos!r}")
    if len(selected_repos) != 6:
        errors.append("Selected engineering work must contain six repository rows")

    seen_repos = set()
    for _, url in links:
        if url.startswith("https://github.com/Yolol100/"):
            repo = url[len("https://github.com/Yolol100/"):].split("/")[0]
            repo = repo.split("?")[0].split("#")[0]
            if repo not in names:
                errors.append(f"Unknown portfolio repository link: {repo}")
            if repo in seen_repos:
                errors.append(f"Repeated portfolio repository link: {repo}")
            seen_repos.add(repo)

    if KEY_RE.search(readme):
        errors.append("Possible secret content in the public profile")
    return errors


def main():
    if len(sys.argv) != 3:
        raise SystemExit("Usage: profile_audit.py README.md github-admin.json")
    readme = Path(sys.argv[1]).read_text(encoding="utf-8")
    config = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    errors = audit_profile(readme, config)
    if errors:
        for error in errors:
            print("FAIL:", error, file=sys.stderr)
        return 1
    print("PASS: profile sections, contacts, case links, unique repository links and central pin order")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
