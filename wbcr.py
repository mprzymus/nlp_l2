import json
import os
from contextlib import redirect_stderr
from pathlib import Path

import fasttext


def calculate_metrics(tp: int, fp: int, fn: int) -> dict[str, float]:
    recall = tp / (tp + fn)
    precision = tp / (tp + fp)
    f1 = 2 * (precision * recall) / (precision + recall)

    return {
        "recall": recall,
        "precision": precision,
        "f1": f1,
    }


def run_tests(embeddings_model: Path, test: Path, k: int = 100):
    with open(os.devnull, "w") as null:
        with redirect_stderr(null):
            model = fasttext.load_model(str(embeddings_model))

    tests = json.loads(test.read_text())
    tests = {test: set(targets) for test, targets in tests.items()}

    tp, fp, fn = 0, 0, 0

    for test, targets in tests.items():
        nns = {word for _, word in model.get_nearest_neighbors(test, k=k)}

        tp += len(targets & nns)
        fp += len(nns - targets)
        fn += len(targets - nns)

    return calculate_metrics(tp, fp, fn)
