from collections import Counter


def convert(text):
    text = dict(Counter(text))
    list_text = []
    for k, v in text.items():
        if v == 1:
            list_text.append(f'{k}')
        else:
            list_text.append(f'{k}{v}')
    text = ''.join(list_text)
    return print(text)


example = input('Enter text: ')
convert(example)
