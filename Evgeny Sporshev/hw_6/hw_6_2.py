from collections import Counter


def letter_counter(letters):
    collection = Counter(letters)

    collection = dict(collection)

    result = ''
    for i in collection:
        result = result + i
        result = result + str(collection[i])

    print(result)


test_string = input('Введите символы: ')
letter_counter(test_string)
