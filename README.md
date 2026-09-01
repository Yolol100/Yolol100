# Yolol100 — WordPress, automatisering en productontwikkeling

Ik bouw praktische software voor contentbeheer, websitekwaliteit, SEO-evidence en game tooling. Mijn repositories combineren productontwikkeling met een sterke nadruk op begrensde automatisering, reproduceerbare tests en veilige integraties.

## Waar ik aan werk

- **WordPress en WooCommerce:** plugins, content-synchronisatie, ACF, Elementor en veilige releasepakketten.
- **Automatisering:** Python-, JavaScript- en GitHub Actions-workflows met expliciete contracten en controleerbare artifacts.
- **Websitekwaliteit:** technische SEO, accessibility-, performance-, markup- en visual-regressie-evidence.
- **Productontwikkeling:** portable Windows-tools en WoW-addons met reproduceerbare releases.

## Uitgelichte projecten

| Project | Wat het oplost | Technologie en bewijs |
| --- | --- | --- |
| [Elementorconnector](https://github.com/Yolol100/Elementorconnector) | Beheerst WordPress-, ACF-, Yoast- en bestaande Elementor-content via een private GitHub-reviewflow met conflictcontrole en rollback. | PHP, WordPress APIs, Composer, wp-env en uitgebreide CI-matrix |
| [KeystoneLens](https://github.com/Yolol100/KeystoneLens) | Combineert een WoW-addon met een portable Windows Companion voor lokale recruitmentanalyse. | Python, Lua, Windows-builds, CodeQL en deterministische packaging |
| [Orchestrator](https://github.com/Yolol100/Orchestrator) | Transporteert goedgekeurde Webactueel-plannen naar begrensde specialistrepositories. | Python, GitHub App-tokens, Actions en contracttests |
| [seochecker](https://github.com/Yolol100/seochecker) | Maakt reproduceerbare technische SEO-audits met optionele Search Console- en Ahrefs-context. | Python, SiteOne, Lighthouse, Nu HTML Checker en run-artifacts |
| [Designchecker](https://github.com/Yolol100/Designchecker) | Levert read-only browser-, accessibility-, performance- en visual-regressie-evidence. | TypeScript, Playwright, axe-core, Lighthouse en Pixelmatch |
| [RaidLeadAssist](https://github.com/Yolol100/RaidLeadAssist) | Biedt fail-closed raidplannen, assignments en handmatige callouts voor WoW. | Lua, WoW Retail APIs en geautomatiseerde validatie |

## Webactueel

De Webactueel-repositories zijn opgezet als specialistische capabilities met duidelijke verantwoordelijkheden:

```text
vraag → workflow/controller → vakspecialist → begrensde uitvoering
                                               ↓
                                      controleerbaar artifact
                                               ↓
                                  readback en vakacceptatie
```

Een gestarte of groene workflow is niet automatisch inhoudelijk geaccepteerd. Klant- en run-specifieke data hoort niet permanent op de publieke default branch.

## Repositoryportfolio

De status hieronder is de portfolio-indeling van september 2026. De technische waarheid en actuele release-informatie blijven per repository leidend.

### Flagship

- [Elementorconnector](https://github.com/Yolol100/Elementorconnector)
- [KeystoneLens](https://github.com/Yolol100/KeystoneLens)
- [Orchestrator](https://github.com/Yolol100/Orchestrator)
- [seochecker](https://github.com/Yolol100/seochecker)
- [Designchecker](https://github.com/Yolol100/Designchecker)
- [RaidLeadAssist](https://github.com/Yolol100/RaidLeadAssist)

### Actief ondersteunend

- [Checklist](https://github.com/Yolol100/Checklist)
- Drie private Webactueel-runtimes zijn eveneens als actief ondersteunend geclassificeerd; namen en interne rollen worden niet op het publieke profiel gedeeld.
- [Content-Sync-Manager](https://github.com/Yolol100/Content-Sync-Manager)
- [MDTPullMarker](https://github.com/Yolol100/MDTPullMarker)
- [transcriberen](https://github.com/Yolol100/transcriberen)
- [vacature-engine](https://github.com/Yolol100/vacature-engine)

### Maintenance

- Eén private WordPress-repository is als maintenance geclassificeerd; de naam wordt niet publiek gedeeld.
- [scan-duplicate-images](https://github.com/Yolol100/scan-duplicate-images)
- [Woocommerce-egaline-calculator](https://github.com/Yolol100/Woocommerce-egaline-calculator)
- [Export-acf-to-csv](https://github.com/Yolol100/Export-acf-to-csv)
- [Dienstenoverzicht](https://github.com/Yolol100/Dienstenoverzicht)
- [Link](https://github.com/Yolol100/Link)
- [Pontifex](https://github.com/Yolol100/Pontifex)
- [cursussen-plugin](https://github.com/Yolol100/cursussen-plugin)
- [Patchrunner](https://github.com/Yolol100/Patchrunner)
- [Ultracache-pro](https://github.com/Yolol100/Ultracache-pro)
- [ACF-Text-Manager](https://github.com/Yolol100/ACF-Text-Manager)
- [translatewordpress](https://github.com/Yolol100/translatewordpress)
- [shutterstock-seo-](https://github.com/Yolol100/shutterstock-seo-)
- [soocool-for-woocommerce](https://github.com/Yolol100/soocool-for-woocommerce)
- [acf-image-auto-filler](https://github.com/Yolol100/acf-image-auto-filler)

### Experiment

- [programmeren](https://github.com/Yolol100/programmeren)
- [doctorcura-core](https://github.com/Yolol100/doctorcura-core)
- [doctorcura-ui](https://github.com/Yolol100/doctorcura-ui)

### Archiefkandidaat

- Eén private, lege repository is intern als archiefkandidaat gemarkeerd; de naam wordt niet publiek gedeeld en de repository is niet verwijderd of gearchiveerd.

## Werkwijze

- Wijzigingen verlopen via branches en pull requests.
- Tests en reproduceerbaar bewijs horen bij releases.
- Automatisering krijgt alleen de minimaal noodzakelijke rechten.
- Publieke repositories bevatten geen credentials, klantdata of run-specifieke waarheid.
- Een ontbrekende open-sourcelicentie betekent dat hergebruik niet automatisch is toegestaan.

## Samenwerken

Gebruik het issue-overzicht van het relevante project voor reproduceerbare bugs of verbetervoorstellen. Deel nooit tokens, privélogs, accountgegevens of klantinhoud in een publiek issue.
