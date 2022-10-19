def lune_check(number):
    lx = list(str(number))
    lx.reverse()  # reversing list
    srev = ''.join(lx)  # make str from list-reverse
    s = srev[0::2]  # slise el.  1, 3, 5 .....
    s2 = srev[1::2]  # slise el.  2, 4, 6 ....

    def calk1(numbers):  # функция подсчета суммы чисел в строке

        summ = 0
        for i in range(len(list(numbers))):
            summ = summ + int(list(numbers)[i])
        return summ

    def calk2(numbers):  # функция подсчета  суммы удвоенных чисел строки
        summ = 0
        for i in range(len(list(numbers))):
            if int(i * 2) > 9:
                e = int(list(str(i * 2))[0]) + int(list(str(i * 2))[1])
            else:
                e = int(i) * 2
            summ = summ + e
        return summ
    sumsum = calk1(s) + calk2(s2)

    print('Lune\'s metod summ: ', sumsum)

    if sumsum % 10 == 0:     # проверка остатка от деления суммы на 10 (алгоритм Луна)
        return True

    else:
        return False


while True:
    card_number = input('Please enter card number: ', )
    print('yor\'s card number : ', card_number)
    if not len(card_number):              # защита от пустой строки
        print('error! field cannot be empty')
        continue

    if not card_number.isdigit():                            # защита от ввода букв
        print("error! card number must contain only digits")
        continue

    if lune_check(card_number) is True:
        print('card number is correct!')
        break

    elif len(card_number) != 16:                             # только 16 -значный номер!
        print('Error! Your\'s number is not 16-digit. Enter 16-digit card number!')

    elif lune_check(card_number) is False:
        print('Error! Your\'s card number is not correct!')
