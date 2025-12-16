from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from pathlib import Path

app = FastAPI()


class RequestItem(BaseModel):
    data: list


MODEL_PATH = Path("models/model.joblib")
MODEL = None
if MODEL_PATH.exists():
    MODEL = joblib.load(MODEL_PATH)


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": MODEL is not None}


@app.post("/predict")
def predict(req: RequestItem):
    if MODEL is None:
        return {"error": "model not available"}
    model = MODEL["model"]
    data = req.data
    preds = model.predict(data)
    return {"predictions": preds.tolist()}
