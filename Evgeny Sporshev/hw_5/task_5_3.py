def len_checker(a):
    if len(str(a)) != 4:
        return False
    else:
        return True


def repeat_checker(c):
    c = str(c)
    i = 0
    while i < len(c):
        if c.count(c[i]) > 1:
            return False
        else:
            i += 1


while True:
    secret_number = input('Игрок 1, загадай четырехзначное число число: ')
    if len_checker(secret_number) is True and repeat_checker(secret_number) is None:
        break
    else:
        print('Ошибка, должно быть четырехзначное число с неповторяющимися числами')

while True:
    while True:
        suggested_number = input('Игрок 2, угадай четырехзначное число число: ')
        if len_checker(suggested_number) is True and repeat_checker(suggested_number) is None:
            break
        else:
            print('Ошибка, должно быть четырехзначное число с неповторяющимися числами')
    cow_counter = 0
    bull_counter = 0
    if suggested_number == secret_number:
        print('Вы выиграли!')
        break
    for i in range(len(suggested_number)):
        if suggested_number[i] == secret_number[i]:
            bull_counter += 1
        elif suggested_number[i] in secret_number:
            cow_counter += 1
        else:
            continue
    print('Коров:', cow_counter, 'Быков:', bull_counter)
