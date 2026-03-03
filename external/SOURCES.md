# External skill sources

We use third-party skill packs via the `skills` CLI.

## Marketing Skills (Corey Haines)
Source repo: https://github.com/coreyhaines31/marketingskills

Install/update (recommended):
```bash
npx skills add coreyhaines31/marketingskills --all --global --yes
npx skills update coreyhaines31/marketingskills
```

Notes:
- These skills are not authored by Laniameda.
- We do not vendor/copy them into this repo by default; we reference them as an upstream source.
- If we customize any skill, fork upstream into `laniameda-skills` and change the install source.
