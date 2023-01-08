import logging
import warnings
from pathlib import Path
from statistics import mean, stdev

import pytorch_lightning as pl

from data import HatefulTweets
from nn import BinaryMLP, train_model


def run_fasttext_test(
    model_file: Path,
    name: str = "model",
    seed: int = 42,
    verbose: bool = True,
) -> dict[str, float]:
    pl.seed_everything(seed, workers=True)

    datamodule = HatefulTweets(model_file, 128)
    model = BinaryMLP(300, [512, 256, 128, 64], learning_rate=1e-4)

    best_log = train_model(model, datamodule, name=name, epochs=200, verbose=verbose)
    return best_log


def run_repeated_fasttext(
    model_file: Path,
    name: str = "model",
    verbose: bool = False,
) -> dict[str, str]:
    logging.getLogger("pytorch_lightning").setLevel(logging.ERROR)

    logs: dict[str, list[float]] = {}

    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", message=".*Checkpoint directory.*")

        for seed in range(1, 11):
            log = run_fasttext_test(
                model_file,
                name=f"{name}_{seed}",
                seed=seed,
                verbose=verbose,
            )

            for k, v in log.items():
                logs.setdefault(k, []).append(v)

    logging.getLogger("pytorch_lightning").setLevel(logging.INFO)

    return {
        key: f"{mean(value):.4f} ± {stdev(value):.4f}" for key, value in logs.items()
    }
