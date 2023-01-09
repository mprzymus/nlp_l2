import json
from pathlib import Path

import plwordnet
from tqdm import tqdm

from config import (
    PLWORDNET,
    WBCR_LEAST_FREQUENT,
    WBCR_MOST_FREQUENT,
    WBCR_TESTS_LEAST,
    WBCR_TESTS_MOST,
)

wn = plwordnet.load(str(PLWORDNET))


def load_nouns(from_: Path) -> list[str]:
    return from_.read_text().splitlines()


def extract_wbcr(
    nouns: list[str],
    out: Path,
    max_hyper: int = 3,
    max_hypo: int = 2,
) -> None:
    final = {}

    for noun in tqdm(nouns):
        tests: set[str] = set()
        words = [w for w in wn.find(noun) if w.pos == "NOUN" and w.synset is not None]
        synsets: list[plwordnet.Synset] = [w.synset for w in words]

        for synset in synsets:
            tests.update(lu.name for lu in synset.lexical_units if lu.pos == "NOUN")

        for paths in (
            wn.hypernym_paths(synset, full_search=True) for synset in synsets
        ):
            for path in paths:
                for i, synset in enumerate(path):
                    if i + 1 > max_hyper:
                        break

                    tests.update(
                        lu.name for lu in synset.lexical_units if lu.pos == "NOUN"
                    )

        current = synsets
        next: list[plwordnet.Synset] = []
        seen = set()
        for i in range(max_hypo):
            for child_synsets in (wn.hyponyms(s) for s in current):
                for synset in child_synsets:
                    seen.add(synset.id)
                    tests.update(
                        lu.name for lu in synset.lexical_units if lu.pos == "NOUN"
                    )

                    if synset.id not in seen:
                        next.append(synset)

            current = next

        tests = {w for w in tests if " " not in w}
        if tests:
            tests.add(noun)

        final[noun] = list(tests)

    out.write_text(json.dumps(final, indent=2))


def main():
    extract_wbcr(load_nouns(WBCR_LEAST_FREQUENT), WBCR_TESTS_LEAST)
    extract_wbcr(load_nouns(WBCR_MOST_FREQUENT), WBCR_TESTS_MOST)


if __name__ == "__main__":
    main()
