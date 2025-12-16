# Docker Hub push instructions

Replace `yourusername` below with your Docker Hub username.

Build and tag image:

```bash
docker build -t mlops-api .
docker tag mlops-api yourusername/mlops-api:v1
```

Login and push:

```bash
docker login
docker push yourusername/mlops-api:v1
```

If you want GitHub Actions to push images, create a GitHub secret `DOCKERHUB_TOKEN` and add a job to the workflow (I can help scaffold this if needed).
