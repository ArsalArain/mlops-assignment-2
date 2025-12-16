# Report template — Assignment 02

Use this template to assemble your PDF/Word report. Fill in each section and attach terminal logs and screenshots.

1. Title and authors

2. Setup commands used
```text
# Virtualenv creation
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

3. Git & DVC commands executed (include terminal logs and screenshots)

- git init / git add / git commit outputs
- dvc init
- dvc remote add -d myremote ./dvcstore
- dvc add data/dataset.csv
- dvc repro

4. CI/CD
- Describe `.github/workflows/ci.yml` and include Actions run screenshot or link.

5. Docker
- Commands used to build/run and evidence (logs, container screenshot).

6. Airflow (if run)

7. REST API
- How you tested `/health` and `/predict` (include Postman/cURL examples and responses).

8. Deployment to AWS (if performed)
- S3 bucket name, object URL, EC2 instance ID, public endpoint.

9. Problems faced & fixes applied

10. Learning summary

Appendix: list of files to include in zipped submission (exclude `.venv`, `data/`, `models/`, `dvcstore`)
