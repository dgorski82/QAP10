from functools import reduce
card_number = input('Please enter credit card number: ')


def luhn(card_number):
    LOOKUP = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)
    card_number = reduce(str.__add__, filter(str.isdigit, card_number))
    evens = sum(int(i) for i in card_number[-1::-2])
    odds = sum(LOOKUP[int(i)] for i in card_number[-2::-2])
    return (evens + odds) % 10 == 0


def card_validation():
    if not card_number.isdigit():
        print('Enter only digits!')
    elif not 13 < len(str(card_number)) < 17:
        print('Check digits amount')
    else:
        if not luhn(card_number):
            print('Invalid credit card number')
        else:
            print('Valid card number')


card_validation()
