def addition(e, r):
    return 'Addition result: ', str(int(e) + int(r))


def subtraction(e, r):
    return 'Subtraction result: ', str(int(e) - int(r))


def multiplication(e, r):
    return 'Multiplication result: ', str(int(e) * int(r))


def division(e, r):
    if int(e) % int(r) == 0:
        return 'Division result: ', str(int(e) / int(r))
    else:
        return 'Division result: ', str(int(e) // int(r)), '  Remainder of division: ', str(int(e) % int(r))


def calc(a, b, oper_type):

    if oper_type == '1':
        return addition(a, b)

    if oper_type == '2':
        return subtraction(a, b)

    if oper_type == '3':
        return multiplication(a, b)

    if oper_type == '4':
        return division(a, b)


print("\nWelcome to Calculator 1.0")

while True:

    operation = input(
        "Please, insert the operation number:\n"
        "  1 - Addition \"x + y\"\n"
        "  2 - Subtraction \"x - y\"\n"
        "  3 - Multiplication \"x * y\"\n"
        "  4 - Division \"x / y\"\n"
        "  >>> ", )

    if operation not in ['1', '2', '3', '4']:  # защита от ввода неверного значения
        print('ERROR! Please insert number from 1 to 4')
        continue
    else:
        digit_1 = input('Please, insert \"x\": ', )
        if not digit_1.isdigit():  # защита от ввода букв
            print("ERROR! This field must contain only digits")
            continue
        else:
            digit_2 = input('Please, insert \"y\": ', )
            if not digit_2.isdigit():  # защита от ввода букв
                print("ERROR! This field must contain only digits")
                continue
            if operation == '4' and int(digit_2) == 0:
                print('can\'t divide by zero')
                continue
            else:
                result = calc(digit_1, digit_2, operation)
                print('x: ', digit_1)
                print('y: ', digit_2)
                print(''.join(result), '\n')
