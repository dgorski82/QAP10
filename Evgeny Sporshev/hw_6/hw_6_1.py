from functools import reduce


def validate(code):
    code = str(code)
    # Предварительно рассчитанные результаты умножения на 2 с вычетом 9 для больших цифр
    # Номер индекса равен числу, над которым проводится операция
    LOOKUP = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)
    code = reduce(str.__add__, filter(str.isdigit, code))
    evens = sum(int(i) for i in code[-1::-2])
    odds = sum(LOOKUP[int(i)] for i in code[-2::-2])
    result = ((evens + odds) % 10 == 0)
    print(result)
    return result


def card_number_checker(number):
    if len(number) == 0:
        print('Введено неверное количество цифр')
        return False
    elif number.isupper() or number.islower():
        print('Буквы не должны присутствовать в строке')
        return False
    else:
        return True


card_number = input('Введите номер карты: ')
if card_number_checker(card_number):
    validate(card_number)
