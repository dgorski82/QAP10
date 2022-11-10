from collections import Counter


def letter_counter(letters):
    msg = Counter(letters)

    msg = dict(msg)

    result = ''
    for i in msg:
        result = result + i
        result = result + str(msg[i])

    print(result)


string_1 = input(': ')
letter_counter(string_1)
