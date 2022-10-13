def counter(s: str) -> list:
    return [len(i) for i in list(s.split(' ')) if i != 'the']


print(counter('the quick brown fox jumps over the lazy dog'))
