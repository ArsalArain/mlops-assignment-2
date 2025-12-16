FROM python:3.10-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=1
WORKDIR /app
COPY . /app
# Install minimal dependencies for training/API to avoid pinned conflicts in requirements.txt
RUN python -m pip install --upgrade pip setuptools wheel \
	&& pip install -r requirements-docker.txt

# default command runs the API with Uvicorn; to run training override the CMD
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
