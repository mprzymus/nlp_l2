import typing as t
from pathlib import Path

import fasttext

from config import (
    CBOW_CORPUS,
    CBOW_FULL,
    CORPUS_SENTENCES,
    FULL_SENTENCES,
    SG_CORPUS,
    SG_FULL,
)


def train_model(
    source: Path,
    output: Path,
    method: t.Literal["skipgram", "cbow"],
    dim: int = 300,
):
    model = fasttext.train_unsupervised(str(source), model=method, dim=dim, thread=20)
    model.save_model(str(output))


def main():
    train_model(CORPUS_SENTENCES, SG_CORPUS, method="skipgram")
    train_model(CORPUS_SENTENCES, CBOW_CORPUS, method="cbow")
    train_model(FULL_SENTENCES, SG_FULL, method="skipgram")
    train_model(FULL_SENTENCES, CBOW_FULL, method="cbow")


if __name__ == "__main__":
    main()
