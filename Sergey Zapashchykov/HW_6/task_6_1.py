credit_card_number = input('Enter card number: ')


def valid_card_number(card_number):
    if len(card_number) == 0 or not card_number.isdigit():
        return 'Input error'
    card_number = card_number[::-1]
    card_number = [int(number) for number in card_number]
    card_number_double_every_second = []
    digits_list = list(enumerate(card_number, start=1))
    for index, digit in digits_list:
        if index % 2 == 0:
            card_number_double_every_second.append(digit * 2)
        else:
            card_number_double_every_second.append(digit)
    summa = 0
    for i in card_number_double_every_second:
        if i < 10:
            summa += i
        else:
            summa += (i % 10) + (i // 10)
    if summa % 10 == 0:
        return 'Valid card number'
    else:
        return 'Invalid card number'


print(valid_card_number(credit_card_number))
