from pathlib import Path
import string
import emoji
from tqdm import tqdm
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, casual_tokenize
from config import CORPUS, FULL, CORPUS_SENTENCES, FULL_SENTENCES

nltk.download("punkt", quiet=True)


def process_file(f: Path, output: Path) -> None:
    translation_table = str.maketrans("", "", string.punctuation + "—ᴗ❛… ️³￣’”„𓆉•♡›«»–")

    with (
        f.open(mode="r", encoding="utf-8") as in_,
        output.open(mode="w", encoding="utf-8") as out,
    ):
        lines = sum(1 for _ in in_)
        in_.seek(0)

        for line in tqdm(in_, total=lines):
            if line == "\n":
                continue

            line = line.replace("@user", "").lower()

            sentences = sent_tokenize(line, language="polish")
            for sentence in sentences:
                words = [
                    word.translate(translation_table)
                    for word in casual_tokenize(sentence)
                    if not word.startswith("#")
                ]

                text = " ".join(
                    word for word in words if word not in emoji.UNICODE_EMOJI
                )
                text = text.replace("  ", " ").strip()

                if text:
                    out.write(text)
                    out.write("\n")


def main():
    process_file(CORPUS, CORPUS_SENTENCES)
    process_file(FULL, FULL_SENTENCES)


if __name__ == "__main__":
    main()
