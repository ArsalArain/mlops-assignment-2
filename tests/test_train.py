import os
from src.train import train


def test_train_creates_model(tmp_path):
    outdir = tmp_path / "models"
    model_path, acc = train(str(outdir))
    assert os.path.exists(model_path)
    assert acc > 0.5
