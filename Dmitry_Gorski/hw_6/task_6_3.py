def multiply(a, b: int) -> int:
    return a * b


def summa(a, b: int) -> int:
    return a + b


def diff(a, b: int) -> int:
    return a - b


def division(a, b: int) -> tuple:
    try:
        x, y = a // b, a % b
        return x, y
    except ZeroDivisionError:
        print('На ноль делить нельзя!!!')


def convert(a, b: str) -> tuple:
    return int(a), int(b)


if __name__ == "__main__":

    choice = input('Выбирите операцию:\n'
                   '1.Сложение\n'
                   '2.Вычитание\n'
                   '3.Умножение\n'
                   '4.Деление\n'
                   'Введите номер пункта меню >>> ')

    assert choice.isdigit() and \
           choice in ('1', '2', '3', '4'), 'Неверный ввод'

    f = input('Введите первое число >>> ')
    assert f.isdigit() or int(f), 'Неверный ввод'

    s = input('Введите второе число >>> ')
    assert s.isdigit() or int(s), 'Неверный ввод'

    match choice:
        case '1':
            print('Сумма: ', summa(*convert(f, s)))
        case '2':
            print('Разность: ', diff(*convert(f, s)))
        case '3':
            print('Произведение: ', multiply(*convert(f, s)))
        case '4':
            print('Частное: {} '
                  'Остаток: {}'.format(*division(*convert(f, s))))
