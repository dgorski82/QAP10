def summa(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    if b != 0:
        result = f'Частное: {int(a // b)}, Остаток: {int(a % b)}'
    else:
        result = "Деление на ноль!"
    return result


operations = input('Введите номер пункта меню:\n 1. Сложение\n 2. Вычитание\n 3. Умножение\n 4. Деление\n ')
if operations not in ('1', '2', '3', '4'):
    quit()
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число '))

if operations == '1':
    print(summa(num1, num2))
elif operations == '2':
    print(sub(num1, num2))
elif operations == '3':
    print(mult(num1, num2))
elif operations == '4':
    print(div(num1, num2))
