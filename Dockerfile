FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip && pip install -r requirements.txt
# default command runs training; API can be started by overriding CMD
CMD ["python", "-m", "src.train", "--output-dir", "models"]
