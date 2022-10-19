def validate_input(func):
    def wrapper(a, b: str):
        assert str(a).isdigit() and str(b).isdigit() or float(a) or float(b), 'Неверный ввод'
        return func(a, b)
    return wrapper


@validate_input
def multiply(a, b: int) -> int:
    return a * b


@validate_input
def summa(a, b: int) -> int:
    return a + b


@validate_input
def diff(a, b: int) -> int:
    return a - b


@validate_input
def division(a, b: int) -> tuple:
    try:
        x, y = a // b, a % b
        return x, y
    except ZeroDivisionError:
        print('На ноль делить нельзя!!!')


def random_count(string: str) -> int:
    assert isinstance(string, str), 'Неверный ввод'
    if all([i.isdigit() or i in ('+', '-', '/', '%', '//', '**') for i in string.replace(' ', '')]):
        return eval(string)
    else:
        print('Это не математическое выражение')


def convert(a, b: str) -> tuple:
    return int(a), int(b)


if __name__ == "__main__":

    choice = input('Выбирите операцию:\n'
                   '1.Сложение\n'
                   '2.Вычитание\n'
                   '3.Умножение\n'
                   '4.Деление\n'
                   '5.Произвольный счет\n'
                   'Введите номер пункта меню >>> ')

    assert choice.isdigit() and \
           choice in ('1', '2', '3', '4', '5'), 'Неверный ввод'

    if choice == '5':
        p = input('Введите математическое выражение >>> ')
        print('Результат: ', random_count(p))
    else:
        f, s = input('Введите первое число >>> '), input('Введите второе число >>> ')
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
