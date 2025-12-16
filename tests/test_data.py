import os
import numpy as np
from src import train as train_module


def test_data_file_exists():
    assert os.path.exists('data/dataset.csv')


def test_load_data_shape():
    X, y = train_module.load_data('data/dataset.csv')
    assert isinstance(X, (list, np.ndarray)) or hasattr(X, 'shape')
    assert hasattr(y, 'shape')
    assert X.shape[0] == y.shape[0]


def test_model_prediction_shape(tmp_path):
    outdir = tmp_path / 'models'
    model_path, acc = train_module.train(str(outdir), data_path='data/dataset.csv')
    model_data = train_module.joblib.load(model_path)
    model = model_data['model']
    X, y = train_module.load_data('data/dataset.csv')
    preds = model.predict(X[:5])
    assert preds.shape[0] == 5
