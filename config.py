import re
from pathlib import Path

CHECKPOINTS_DIR = Path("checkpoints")
DATA_DIR = Path("data")
LOGS_DIR = Path("logs")
OUTPUTS_DIR = Path("outputs")
MODELS_DIR = Path("models")

OUTPUTS_DIR.mkdir(exist_ok=True)
MODELS_DIR.mkdir(exist_ok=True)

FULL = DATA_DIR / "full.txt"
CORPUS = DATA_DIR / "corpus.txt"
PLWORDNET = DATA_DIR / "plwordnet_4_2.xml"
NOUN_FREQ = DATA_DIR / "noun_freq.txt"

SG_FULL = MODELS_DIR / "sg_full.bin"
SG_CORPUS = MODELS_DIR / "sg_corpus.bin"
CBOW_FULL = MODELS_DIR / "cbow_full.bin"
CBOW_CORPUS = MODELS_DIR / "cbow_corpus.bin"
PRETRAINED = MODELS_DIR / "pretrained.bin"
KOCON_SKIPGRAM = MODELS_DIR / "kgr10.plain.skipgram.dim300.neg10.bin"
KOCON_CBOW = MODELS_DIR / "kgr10.plain.cbow.dim300.neg10.bin"

PROBLEM_TRAIN = OUTPUTS_DIR / "problem_train.csv"
PROBLEM_TEST = OUTPUTS_DIR / "problem_test.csv"
FULL_SENTENCES = OUTPUTS_DIR / "full_sentences.txt"
CORPUS_SENTENCES = OUTPUTS_DIR / "corpus_sentences.txt"
WBCR_MOST_FREQUENT = OUTPUTS_DIR / "wbcr_most.txt"
WBCR_LEAST_FREQUENT = OUTPUTS_DIR / "wbcr_least.txt"
WBCR_TESTS_LEAST = OUTPUTS_DIR / "wbcr_tests_least.json"
WBCR_TESTS_MOST = OUTPUTS_DIR / "wbcr_tests_most.json"

CONTENT_LINK_REGEX = re.compile(r"https?://t.co/[a-zA-Z0-9]+")
