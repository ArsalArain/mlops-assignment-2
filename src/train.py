import os
import argparse
from pathlib import Path
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def train(output_dir: str):
    """Train a tiny model on Iris and save the artifact to `output_dir`."""
    X, y = load_iris(return_X_y=True)
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
    args = parser.parse_args()
    train(args.output_dir)


if __name__ == "__main__":
    main()
