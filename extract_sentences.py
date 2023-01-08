import string
from pathlib import Path

from tqdm import tqdm

from config import CORPUS, CORPUS_SENTENCES, FULL, FULL_SENTENCES
from text_processing import clean_to_sentences


def process_file(f: Path, output: Path) -> None:
    with (
        f.open(mode="r", encoding="utf-8") as in_,
        output.open(mode="w", encoding="utf-8") as out,
    ):
        lines = sum(1 for _ in in_)
        in_.seek(0)

        for line in tqdm(in_, total=lines):
            if line == "\n":
                continue

            for sent in clean_to_sentences(line):
                out.write(sent)
                out.write("\n")


def main():
    process_file(CORPUS, CORPUS_SENTENCES)
    process_file(FULL, FULL_SENTENCES)


if __name__ == "__main__":
    main()
