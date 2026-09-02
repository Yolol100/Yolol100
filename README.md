# WordPress / WooCommerce / Elementor Developer & Web Automation Builder

I build production-minded WordPress plugins and automation/QA tooling, with a focus on safe content workflows, testable releases and reproducible evidence.

**Open to:** WordPress, WooCommerce, Elementor, PHP and web automation roles.  
**Core stack:** WordPress · WooCommerce · Elementor · ACF · Yoast SEO · PHP · Python · TypeScript/JavaScript · GitHub Actions · Playwright · Lighthouse

## Recruiter snapshot

- Build and maintain WordPress and WooCommerce plugins, content workflows and Elementor/ACF integrations.
- Automate testing, packaging and releases with GitHub Actions and reproducible build checks.
- Work across technical SEO, accessibility, performance, browser automation and visual regression testing.
- Prefer least-privilege integrations, explicit validation, staging-first changes and rollback paths.
- Keep public repositories free of credentials, customer data and run-specific private information.

## Selected projects

These are the best starting points for reviewing my work.

| Project | What it demonstrates | Stack / evidence |
| --- | --- | --- |
| [Elementorconnector](https://github.com/Yolol100/Elementorconnector) | A controlled WordPress content bridge for core content, ACF, Yoast and existing Elementor documents, with conflict detection and verified rollback. | PHP, WordPress APIs, Composer, wp-env, GitHub Actions, integration matrices |
| [Content-Sync-Manager](https://github.com/Yolol100/Content-Sync-Manager) | WordPress content and media export/import tooling with ACF/WooCommerce support, preview-before-write checks and guarded media updates. | PHP, WordPress, ACF, WooCommerce, CI, package validation |
| [seochecker](https://github.com/Yolol100/seochecker) | Reproducible technical SEO audits that separate live technical evidence from optional Search Console and Ahrefs context. | Python, GitHub Actions, SiteOne, Lighthouse CI, Nu HTML Checker |
| [Designchecker](https://github.com/Yolol100/Designchecker) | Read-only browser, accessibility, performance, markup and visual-regression evidence for website QA. | TypeScript, Playwright, axe-core, Lighthouse, Pixelmatch, Sharp |
| [Orchestrator](https://github.com/Yolol100/Orchestrator) | A least-privilege GitHub transport/orchestration layer for bounded automation workflows and inspectable artifacts. | Python, GitHub Actions, GitHub App tokens, contract tests |

## Two-minute technical review

For a fast technical assessment, each flagship exposes implementation, tests and CI directly:

- **Elementorconnector:** [implementation](https://github.com/Yolol100/Elementorconnector/tree/main/includes) · [tests](https://github.com/Yolol100/Elementorconnector/tree/main/tests) · [CI](https://github.com/Yolol100/Elementorconnector/tree/main/.github/workflows)
- **Content-Sync-Manager:** [implementation](https://github.com/Yolol100/Content-Sync-Manager/tree/main/includes) · [tests](https://github.com/Yolol100/Content-Sync-Manager/tree/main/tests) · [CI](https://github.com/Yolol100/Content-Sync-Manager/tree/main/.github/workflows)
- **seochecker:** [implementation](https://github.com/Yolol100/seochecker/tree/main/scripts) · [tests](https://github.com/Yolol100/seochecker/tree/main/tests) · [CI](https://github.com/Yolol100/seochecker/tree/main/.github/workflows)
- **Designchecker:** [implementation](https://github.com/Yolol100/Designchecker/tree/main/src) · [tests](https://github.com/Yolol100/Designchecker/tree/main/tests) · [CI](https://github.com/Yolol100/Designchecker/tree/main/.github/workflows)
- **Orchestrator:** [implementation](https://github.com/Yolol100/Orchestrator/tree/main/scripts) · [tests](https://github.com/Yolol100/Orchestrator/tree/main/tests) · [CI](https://github.com/Yolol100/Orchestrator/tree/main/.github/workflows)

## What I focus on

### WordPress & WooCommerce

Custom plugins, content synchronization, ACF, Elementor, Yoast SEO, media workflows, safe imports/exports and release packaging.

### Automation & delivery

Python/JavaScript automation, GitHub Actions, CI gates, reproducible builds, artifact-based workflows and controlled release processes.

### Website quality

Technical SEO, accessibility, browser automation, performance, HTML validation and visual regression testing.

### Engineering beyond WordPress

I also build portable Windows tooling and World of Warcraft addons. See [KeystoneLens](https://github.com/Yolol100/KeystoneLens) and [RaidLeadAssist](https://github.com/Yolol100/RaidLeadAssist) for Python/Lua and release-engineering examples.

## How I work

- Changes are developed through branches and pull requests where appropriate.
- Tests and reproducible evidence are part of release work, not an afterthought.
- Automation receives only the permissions it needs.
- Risky content changes use validation, staging, conflict checks and rollback where applicable.
- Public repositories do not contain credentials, customer data or private runtime state.

## For hiring managers

If you only have a few minutes, start with **Elementorconnector**, **Content-Sync-Manager**, **seochecker**, **Designchecker** and **Orchestrator**. Together they show WordPress/PHP development, automation, CI/release engineering, SEO/QA tooling and security-conscious integration work.
