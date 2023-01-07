import fasttext
from pathlib import Path
from config import (
    CORPUS_SENTENCES,
    FULL_SENTENCES,
    SG_CORPUS,
    SG_FULL,
    CBOW_CORPUS,
    CBOW_FULL,
)
import typing as t


def train_model(
    source: Path,
    output: Path,
    method: t.Literal["skipgram", "cbow"],
):
    model = fasttext.train_unsupervised(str(source), model=method, thread=20)
    model.save_model(str(output))


def main():
    train_model(CORPUS_SENTENCES, SG_CORPUS, method="skipgram")
    train_model(CORPUS_SENTENCES, CBOW_CORPUS, method="cbow")
    train_model(FULL_SENTENCES, SG_FULL, method="skipgram")
    train_model(FULL_SENTENCES, CBOW_FULL, method="cbow")


if __name__ == "__main__":
    main()
