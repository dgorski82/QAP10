test_false = 4561261212345464
test_true = 4561261212345467


def validate(card_num):
    card_list = list(map(int, str(card_num)))

    if len(card_list) % 2 == 0:
        start = 0
        start_alt = 1
        last_num = 0
    else:
        last_num = card_list[-1]
        start = 1
        start_alt = 0

    list_output = []
    for digital, digital_alt in zip(card_list[start::2], card_list[start_alt::2]):
        digital *= 2
        digital -= 9 * (digital > 9)
        list_output.append(digital)
        list_output.append(digital_alt)
    return (sum(list_output) + last_num) % 10 == 0


print(validate(test_false))
print(validate(test_true))
print(validate(371449635398431))
