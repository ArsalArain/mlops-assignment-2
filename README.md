# MLOps Assignment 2 — Project

This repository contains the student project for MLOps Assignment 2. It includes code, tests, a DVC pipeline, a simple FastAPI inference app and a Dockerfile.

Quick start (Windows PowerShell):

```powershell
cd C:\Users\ALLAH\mlops_assignment_2
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

Run tests:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pytest -q
```

Run training (local):

```powershell
python -m src.train --output-dir models --data-path data/dataset.csv
```

Run FastAPI locally:

```powershell
pip install -r requirements-dev.txt
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
# then visit http://localhost:8000/health
```

Run with Docker (build + run API):

```powershell
docker build -t mlops-api .
docker run -d -p 8000:8000 --name mlops-api mlops-api
```

Docker Hub push (example): see DOCKER_PUSH.md for commands and notes.

DVC usage (local):

```powershell
.\.venv\Scripts\Activate.ps1
python -m dvc init
python -m dvc remote add -d myremote ./dvcstore
python -m dvc add data/dataset.csv
python -m dvc repro
```

Repository layout (important files):
- `src/` — source code (training)
- `api/` — FastAPI app
- `tests/` — pytest tests
- `dvc.yaml`, `dvc.lock` — DVC pipeline
- `Dockerfile`, `docker-compose.yml` — containerization

If you need any of the deliverable screenshots or logs, run the commands above and save terminal output or use the provided helper snippets in `REPORT_TEMPLATE.md`.
# MLOps Assignment 2 — Project Setup

This repository contains the initial project structure for the assignment.

Quick setup (Windows PowerShell):

```powershell
cd C:\Users\ALLAH\mlops_assignment_2
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Folders created:
- `src` — source code
- `data` — data storage (gitignored)
- `notebooks` — Jupyter notebooks
- `models` — saved models (gitignored)

Files:
- `.gitignore` — ignores venv, data, models
- `requirements.txt` — dependency list
