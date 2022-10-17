def is_number(str_1):
    count_dots = 0
    for i in range(len(str_1)):
        if i == 0 and not (str_1[i] == "-" or str_1[i].isdigit()):
            print("1")
            return False
        elif str_1[i] == "." and i != 0:
            print("2")
            count_dots += 1
            if count_dots > 1:
                return False
        elif i != 0 and not str_1[i].isdigit():
            print("3")
            print(str_1[i])
            return False
    return True


def calc(val_1, val_2, oper):
    if oper == "1":
        return val_1 + val_2
    elif oper == "2":
        return val_1 - val_2
    elif oper == "3":
        return val_1 * val_2
    elif oper == "4":
        if float(val_2) == 0:
            print("На 0 делить нельзя")
            return
        return int(val_1 / val_2), int(val_1 % val_2)


while True:
    operation = input("Выберите операцию:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n")
    if not operation.isdigit() or "1, 2, 3, 4".find(operation) < 0:
        print("Выбрана некорректная операция")
        break
    else:
        a = input("Введите первое число\n")
        b = input("Введите второе число\n")
        if not is_number(a) or not is_number(b):
            print("Введены некорретные числа")
            continue
        else:
            if operation == "4":
                ch = calc(float(a), float(b), operation)
                if ch is not None:
                    print(f"Результат деления: частное - {ch[0]}, остаток - {ch[1]}")
            else:
                print(f"Результат операции: {calc(float(a), float(b), operation)}")
