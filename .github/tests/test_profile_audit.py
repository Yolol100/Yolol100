"""Regression scenarios for the GitHub profile presentation contract."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from profile_audit import audit_profile


PINS = [
    "ACF-Text-Manager",
    "soocool-for-woocommerce",
    "Content-Sync-Manager",
    "theme",
    "Designchecker",
    "Ultracache-pro",
]


def sample():
    rows = "\n".join(
        f"| [{name}](https://github.com/Yolol100/{name}) | Example project |"
        for name in PINS
    )
    readme = (
        "# WordPress Developer & Web Designer\n\n"
        "[Portfolio](https://andrewbaeten.nl/#cases) · "
        "[LinkedIn](https://www.linkedin.com/in/example/) · "
        "[Email](mailto:info@example.com)\n\n"
        "## Start here\n\nStart with the portfolio.\n\n"
        "## Website & design cases\n\n"
        "[Case 1](https://andrewbaeten.nl/casareno/) · "
        "[Case 2](https://andrewbaeten.nl/byderma/) · "
        "[Case 3](https://andrewbaeten.nl/acf-page-text-manager/)\n\n"
        "## Selected engineering work\n\n"
        "| Project | Description |\n| --- | --- |\n"
        + rows
        + "\n\n## More projects by area\n\n"
        "[SEO Checker](https://github.com/Yolol100/seochecker)\n\n"
        "## How I work\n\nWith tests.\n\n"
        "## Background & contact\n\nWordPress developer.\n"
    )
    config = {
        "owner": "Yolol100",
        "repositories": [{"name": x} for x in PINS + ["seochecker"]],
        "profile": {"desired_pins": list(PINS)},
    }
    return readme, config


class ProfileAuditTests(unittest.TestCase):
    def test_valid_profile(self):
        readme, config = sample()
        self.assertEqual(audit_profile(readme, config), [])

    def assert_rejected(self, readme, config):
        issues = audit_profile(readme, config)
        self.assertTrue(issues, "Expected profile audit to reject modified input")

    def test_missing_headline(self):
        a, c = sample()
        self.assert_rejected(a.replace("# WordPress Developer", "# Developer"), c)

    def test_missing_portfolio(self):
        a, c = sample()
        self.assert_rejected(a.replace("https://andrewbaeten.nl/#cases", "https://example.com"), c)

    def test_missing_linkedin(self):
        a, c = sample()
        self.assert_rejected(a.replace("https://www.linkedin.com/in/example/", "https://example.com"), c)

    def test_missing_contact(self):
        a, c = sample()
        self.assert_rejected(a.replace("mailto:info@example.com", "https://example.com"), c)

    def test_missing_case(self):
        a, c = sample()
        self.assert_rejected(a.replace("[Case 3](https://andrewbaeten.nl/acf-page-text-manager/)", ""), c)

    def test_duplicate_case_does_not_count_as_three(self):
        a, c = sample()
        self.assert_rejected(a.replace("https://andrewbaeten.nl/byderma/", "https://andrewbaeten.nl/casareno/"), c)

    def test_missing_section(self):
        a, c = sample()
        self.assert_rejected(a.replace("## How I work", "## My other work"), c)

    def test_duplicate_section(self):
        a, c = sample()
        self.assert_rejected(a + "\n## How I work\n\nDuplicated.\n", c)

    def test_reordered_pins(self):
        a, c = sample()
        first = f"| [{PINS[0]}](https://github.com/Yolol100/{PINS[0]})"
        second = f"| [{PINS[1]}](https://github.com/Yolol100/{PINS[1]})"
        a = a.replace(first, "TEMP_ENTRY").replace(second, first).replace("TEMP_ENTRY", second)
        self.assert_rejected(a, c)

    def test_missing_pin(self):
        a, c = sample()
        line = f"| [{PINS[-1]}](https://github.com/Yolol100/{PINS[-1]}) | Example project |\n"
        self.assert_rejected(a.replace(line, ""), c)

    def test_duplicate_repository_link(self):
        a, c = sample()
        self.assert_rejected(a + "\n[Again](https://github.com/Yolol100/Designchecker)\n", c)

    def test_distinct_verification_deep_link_is_allowed(self):
        a, c = sample()
        deep_link = "[Verification](https://github.com/Yolol100/ACF-Text-Manager#verification)"
        a = a.replace("Example project", deep_link, 1)
        self.assertEqual(audit_profile(a, c), [])

    def test_repeated_deep_link_is_rejected(self):
        a, c = sample()
        deep_link = "[Verification](https://github.com/Yolol100/ACF-Text-Manager#verification)"
        a = a.replace("Example project", deep_link, 1)
        self.assert_rejected(a + "\n" + deep_link + "\n", c)

    def test_duplicate_root_link_with_trailing_slash_is_rejected(self):
        a, c = sample()
        self.assert_rejected(
            a + "\n[Repeat](https://github.com/Yolol100/ACF-Text-Manager/)\n", c
        )

    def test_unknown_repository(self):
        a, c = sample()
        self.assert_rejected(a + "\n[Unknown](https://github.com/Yolol100/not-a-real-project)\n", c)

    def test_wrong_config_owner(self):
        a, c = sample()
        c["owner"] = "OtherOwner"
        self.assert_rejected(a, c)

    def test_config_missing_pin_repository(self):
        a, c = sample()
        c["repositories"] = [x for x in c["repositories"] if x["name"] != PINS[0]]
        self.assert_rejected(a, c)

    def test_duplicate_config_pins(self):
        a, c = sample()
        c["profile"]["desired_pins"][-1] = PINS[0]
        self.assert_rejected(a, c)

    def test_secret_marker(self):
        a, c = sample()
        self.assert_rejected(a + "\n-----BEGIN OPENSSH PRIVATE KEY-----\n", c)


if __name__ == "__main__":
    unittest.main()
