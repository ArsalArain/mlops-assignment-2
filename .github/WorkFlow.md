<!-- Auto-generated guidance for AI coding agents working in this repo -->
# Copilot instructions — MLOps Assignment 2

Purpose: Help AI coding agents be immediately productive in this repository by describing the project's layout, developer workflows, conventions, and concrete examples to reference.

**Quick Setup**:
- **Windows PowerShell:** follow the project README setup to create and activate the venv and install deps:

```powershell
cd C:\Users\ALLAH\mlops_assignment_2
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Key files / places to inspect**:
- **Project root:** [README.md](README.md#L1) — setup and high-level notes.
- **Source package:** [src/__init__.py](src/__init__.py#L1) — primary application code lives under `src/`.
- **Data & artifacts:** `data/` and `models/` are present and gitignored — treat them as large / ephemeral artifacts.
- **Notebooks:** `notebooks/` contains analysis and experiments; prefer refactoring stable code from notebooks into `src/`.
- **Tests:** `tests/` — run with `pytest` if present; use it to validate changes.

**Big-picture architecture (discoverable from repo)**:
- Small, single-repo MLOps assignment: code in `src/`, experiments in `notebooks/`, and persisted artifacts in `models/`.
- There are no visible microservices or external orchestration configs — focus on local scripts, data processing, training, and model save/load flows.
- Typical dataflow: notebook/CLI -> code in `src/` -> saved artifacts under `models/`.

**Developer workflows & commands**:
- Create & activate venv, then `pip install -r requirements.txt` (README shows Windows PowerShell commands).
- Run tests: `pytest` from repo root (install `pytest` in venv if not already present).
- Lint/format: not enforced in repo; prefer minimal, consistent formatting when editing existing files.

**Project-specific conventions & patterns**:
- Keep long-lived logic in `src/` and avoid committing large data/model files (they are gitignored).
- Notebooks are for exploration only — when generating production-ready code, extract it to `src/` and add tests in `tests/`.
- Follow existing import/package layout at `src/` (single top-level package).

**Dependencies & integrations**:
- Dependencies are listed in `requirements.txt` at the repo root — inspect before adding packages.
- No cloud or external API configuration files were found — assume local-only runs unless the user provides credentials/config.

**When merging or updating this file**:
- If a pre-existing `.github/copilot-instructions.md` exists, preserve any custom agent guidance and merge repository-specific setup and examples from this file.

**Concrete example prompts for an agent working here**:
- "Refactor notebook `notebooks/my_experiment.ipynb` by extracting data-loading and model-training code into `src/training.py`, add a small CLI, and create tests in `tests/test_training.py`."
- "Run `pytest` and fix any failing tests; only change files under `src/` and `tests/` unless a dependency must be updated in `requirements.txt`."

If anything in this guidance is unclear or you want more specificity (examples of common file patterns, preferred test commands, or CI hooks), tell me which area to expand.
