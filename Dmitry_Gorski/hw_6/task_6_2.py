from collections import Counter


def letter_counter(s: str) -> str:
    assert isinstance(s, str)
    return ''.join([f'{k}{v}' for k, v in Counter(s).items()])
