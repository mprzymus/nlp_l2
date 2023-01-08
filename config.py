import re
from pathlib import Path

CHECKPOINTS_DIR = Path("checkpoints")
DATA_DIR = Path("data")
LOGS_DIR = Path("logs")
MODELS_DIR = Path("models")
MODELS_DIR.mkdir(exist_ok=True)

FULL = DATA_DIR / "full.txt"
CORPUS = DATA_DIR / "corpus.txt"
PROBLEM_TRAIN = DATA_DIR / "problem_train.csv"
PROBLEM_TEST = DATA_DIR / "problem_test.csv"

FULL_SENTENCES = DATA_DIR / "full_sentences.txt"
CORPUS_SENTENCES = DATA_DIR / "corpus_sentences.txt"

SG_FULL = MODELS_DIR / "sg_full.bin"
SG_CORPUS = MODELS_DIR / "sg_corpus.bin"
CBOW_FULL = MODELS_DIR / "cbow_full.bin"
CBOW_CORPUS = MODELS_DIR / "cbow_corpus.bin"
PRETRAINED = MODELS_DIR / "pretrained.bin"
KOCON = MODELS_DIR / "kocon.bin"

CONTENT_LINK_REGEX = re.compile(r"https?://t.co/[a-zA-Z0-9]+")
