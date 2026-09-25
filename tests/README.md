# Tests

Checks that need no hardware, no credits and no qBraid API key.

```bash
pip install -r requirements/core.txt -r requirements/chem.txt
python tests/check_notebooks.py            # everything (a few minutes)
python tests/check_notebooks.py --static   # structure only (seconds)
python tests/check_notebooks.py algorithms # one folder
```

**Static checks** on every notebook: valid JSON saved without outputs; metadata (`notebook_id`, `version`, `level`, `subjects`); analytics tags in the form `quest-<folder>-<notebook>-<milestone>` with all four milestones (`setup`, `simulate`, `hardware`, `compare`); every qBraid hardware submission passes `tags=QUEST_JOB_TAGS`; every code cell compiles; relative links in the notebooks and the top-level Markdown files resolve.

**Execution:** each notebook runs top to bottom in a fresh namespace and stops at its first hardware cell. The introductory notebooks keep `RUN_ON_HARDWARE = False`, so they run completely.

The static checks run on every push through `.github/workflows/checks.yml`. Hardware behaviour is not tested here: that costs credits and is run by hand before each release.
