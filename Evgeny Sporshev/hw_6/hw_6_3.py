from functools import reduce

print('Выберите операцию:\n 1. Сложение \n 2. Вычитание \n 3. Умножение \n 4. Деление')


def menu_choosing():
    while True:
        operation_type = input('Введите номер операции: ')
        if operation_type not in ['1', '2', '3', '4']:
            print('Введен неверный номер, попробуйте еще раз.')
        else:
            return operation_type


def first_number_choosing():
    while True:
        first_number = input('Введите первое число: ')
        if not first_number.isdigit():
            print('Буквы вводить не надо')
        else:
            return int(first_number)


def second_number_choosing():
    while True:
        second_number = input('Введите второе число: ')
        if not second_number.isdigit():
            print('Буквы вводить не надо')
        elif second_number == '0' and operation == '4':
            print('На ноль делить не будем')
        else:
            return int(second_number)


operation = menu_choosing()
number_one = first_number_choosing()
number_two = second_number_choosing()
items = [number_one, number_two]

if operation == '1':
    addition_items = reduce(lambda x, y: x + y, items)
    print(addition_items)
elif operation == '2':
    subtraction_items = reduce(lambda x, y: x - y, items)
    print(subtraction_items)
elif operation == '3':
    multiplication_items = reduce(lambda x, y: x * y, items)
    print(multiplication_items)
else:
    division_items_quotient = reduce(lambda x, y: x // y, items)
    division_items_euclidean = reduce(lambda x, y: x % y, items)
    print(f'Частное: {division_items_quotient}, Остаток: {division_items_euclidean}')
