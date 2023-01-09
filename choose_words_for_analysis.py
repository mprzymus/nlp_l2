import pandas as pd
import plwordnet

from config import NOUN_FREQ, PLWORDNET, WBCR_LEAST_FREQUENT, WBCR_MOST_FREQUENT

wn = plwordnet.load(str(PLWORDNET))


def process_words(words: pd.Series) -> str:
    unique = {w for w in words if "." not in w}
    to_save = {
        lu.name.lower()
        for w in unique
        for lu in wn.find(w)
        if lu.language == "pl" and lu.pos == "NOUN"
    }
    return "\n".join(to_save)


def extract_most_frequent(frequencies: pd.DataFrame, min_freq: int = 50_000) -> None:
    selected = frequencies[frequencies["freq"] > min_freq]
    processed = process_words(selected["word"])
    WBCR_MOST_FREQUENT.write_text(processed)


def extract_least_frequent(
    frequencies: pd.DataFrame,
    min_freq: int = 350,
    max_freq: int = 500,
) -> None:
    selected = frequencies[
        (frequencies["freq"] > min_freq) & (frequencies["freq"] < max_freq)
    ]
    processed = process_words(selected["word"])
    WBCR_LEAST_FREQUENT.write_text(processed)


def main():
    frequencies = pd.read_csv(NOUN_FREQ, sep="\t", header=None, names=["word", "freq"])

    # extract_most_frequent(frequencies)
    extract_least_frequent(frequencies)


if __name__ == "__main__":
    main()
