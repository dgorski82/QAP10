def calc():

    operations = input('Введите номер пункта меню:\n 1. Сложение\n 2. Вычитание\n 3. Умножение\n 4. Деление\n '
                       '5. Математический пример\n ')
    if operations in ('1', '2', '3', '4'):

        num1 = float(input('Введите первое число: '))
        num2 = float(input('Введите второе число '))

        if operations == '1':
            print(num1 + num2)
        elif operations == '2':
            print(num1 - num2)
        elif operations == '3':
            print(num1 * num2)
        elif operations == '4':
            if num2 != 0:
                print(f'Частное: {int(num1 // num2)}, Остаток: {int(num1 % num2)}')
            else:
                print("Деление на ноль!")

    elif operations in '5':
        math_example = input('Введите математический пример: ')
        print(eval(math_example))


calc()
