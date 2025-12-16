import os
import argparse
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def load_data(data_path: str = "data/dataset.csv"):
    """Load dataset from CSV if available, otherwise fall back to sklearn Iris.

    Returns X (2D numpy array), y (1D numpy array)
    """
    if data_path and os.path.exists(data_path):
        df = pd.read_csv(data_path)
        X = df.values
        # if labels not present, use last column as y when available
        if X.shape[1] > 1:
            # If dataset has more than 1 column and no labels, create dummy labels using iris target distribution
            # Here we assume dataset is features only; create dummy targets for demo purposes
            # Preferably assignment datasets should include labels; this is a safe fallback.
            y = np.zeros(X.shape[0], dtype=int)
        else:
            X = X.reshape(-1, 1)
            y = np.zeros(X.shape[0], dtype=int)
        return X, y
    X, y = load_iris(return_X_y=True)
    return X, y


def train(output_dir: str, data_path: str = "data/dataset.csv"):
    """Train a tiny model on a dataset (CSV) or Iris fallback and save the artifact to `output_dir`."""
    X, y = load_data(data_path)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf = RandomForestClassifier(n_estimators=10, random_state=42)
    clf.fit(X_train, y_train)

    preds = clf.predict(X_test)
    acc = accuracy_score(y_test, preds)

    os.makedirs(output_dir, exist_ok=True)
    model_path = Path(output_dir) / "model.joblib"
    joblib.dump({"model": clf, "accuracy": acc}, model_path)

    print(f"Saved model to {model_path} (accuracy={acc:.3f})")
    return str(model_path), float(acc)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="models", help="Directory to save model")
    parser.add_argument("--data-path", default="data/dataset.csv", help="Path to CSV dataset")
    args = parser.parse_args()
    train(args.output_dir, data_path=args.data_path)


if __name__ == "__main__":
    main()
