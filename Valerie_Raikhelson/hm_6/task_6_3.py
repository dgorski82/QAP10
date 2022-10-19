def num_1():
    return float(input("Введите первое число:"))


def num_2():
    return float(input("Введите второе число:"))


def select_operation():
    return input("Выберите операцию:"
                 "\n1. Сложение"
                 "\n2. Вычитание"
                 "\n3. Умножение"
                 "\n4. Деление "
                 "\nВведите номер пункта меню:")


op = select_operation()


def calculate():
    if op == "1":
        print(num_1() + num_2())
    elif op == "2":
        print(num_1() - num_2())
    elif op == "3":
        print(num_1() * num_2())
    elif op == "4":
        dividend = num_1()
        divisor = num_2()
    assert divisor != 0, 'Divisor cannot be zero'
    print(dividend / divisor)


calculate()
