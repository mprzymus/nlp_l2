from pathlib import Path

DATA_DIR = Path("data")
MODELS_DIR = Path("models")
MODELS_DIR.mkdir(exist_ok=True)

FULL = DATA_DIR / "full.txt"
CORPUS = DATA_DIR / "corpus.txt"

FULL_SENTENCES = DATA_DIR / "full_sentences.txt"
CORPUS_SENTENCES = DATA_DIR / "corpus_sentences.txt"

SG_FULL = MODELS_DIR / "sg_full.bin"
SG_CORPUS = MODELS_DIR / "sg_corpus.bin"
CBOW_FULL = MODELS_DIR / "cbow_full.bin"
CBOW_CORPUS = MODELS_DIR / "cbow_corpus.bin"
