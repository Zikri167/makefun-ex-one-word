"""One word for an ex: PreOwned — love, previously owned."""

WORD = "PreOwned"


def main() -> None:
    """Validate the word and print it, nothing else."""
    assert WORD.isalpha() and WORD.isascii()
    assert len(WORD.split()) == 1
    assert 1 <= len(WORD) <= 111
    print(WORD)


if __name__ == "__main__":
    main()
