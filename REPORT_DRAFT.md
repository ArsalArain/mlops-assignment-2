# Assignment 2 — Report (Draft)

Student: __
Date: 2025-12-16

## 1. Setup & commands used

Virtual environment and dependencies:
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

DVC & data:
```
python -m dvc init
python -m dvc remote add -d myremote ./dvcstore
python -m dvc add data/dataset.csv
python -m dvc repro
```

Docker (build & run API):
```
docker build -t mlops-api .
docker run -d -p 8000:8000 --name mlops-api mlops-api
```

## 2. What I implemented (summary)
- Git initialized, `.gitignore` added, venv created.
- DVC initialized and dataset added. `dvc.yaml` stage `train_model` created; `dvc repro` produced `models/model.joblib`.
- `src/train.py` trains a RandomForest on Iris (or CSV) and saves model.
- Tests in `tests/` added and passing (`pytest` shows 4 passed).
- FastAPI app at `api/main.py` with `/health` and `/predict`.
- Dockerfile + docker-compose to run API; built and container runs locally.
- GitHub Actions CI workflow added to run tests and flake8; new optional Docker publish workflow added.

## 3. Problems faced & fixes
- Large pinned `requirements.txt` caused Docker pip install failures (networkx pinned versions incompatible). Fixed by adding `requirements-docker.txt` with minimal packages for the container.
- Git CLI initially not on PATH — installed and restarted shell.

## 4. How to reproduce and screenshots to include
Include screenshots of:
- Folder structure (file explorer)
- `git init`/git commit outputs
- `dvc add` and `dvc repro` outputs and `data/dataset.csv.dvc`
- pytest results
- Docker build logs and running container (`docker ps`) and `/health` endpoint response
- GitHub Actions run page for `ci.yml`

## 5. Deliverables checklist
- [x] GitHub repo link
- [x] DVC pipeline files
- [x] Tests
- [x] Dockerfile and docker-compose
- [ ] Docker Hub image (optional — push required)
- [ ] Airflow UI screenshot (optional — run compose)
- [ ] AWS deployment (optional)

Appendix: include command logs as text files.
