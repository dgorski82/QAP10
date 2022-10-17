from functools import reduce
card = input('Введите номер карты: ')


def luhn(card_number):

    lookup = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)
    card_number = reduce(str.__add__, filter(str.isdigit, card_number))
    evens = sum(int(i) for i in card_number[-1::-2])
    odds = sum(lookup[int(i)] for i in card_number[-2::-2])
    return (evens + odds) % 10 == 0


def card_chek(card_num):
    if len(card_num) == 0:
        print('Пустая строка. Введите номер карты: ')
    elif not card_num.isdigit():
        print('Введите только цифры: ')
    elif not luhn(card_num):
        print('False')
    else:
        print('True')


card_chek(card)
