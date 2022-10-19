from functools import reduce


def insert_number():
    while True:
        number = input("Enter credit card number: ")
        if number.isdigit() and 12 < len(number) < 17:
            break
    return number


cc_num = insert_number()


def luhn(code):
    LOOKUP = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)
    code = reduce(str.__add__, list(filter(str.isdigit, code)))
    evens = sum(int(i) for i in code[-1::-2])
    odds = sum(LOOKUP[int(i)] for i in code[-2::-2])
    return ((evens + odds) % 10 == 0)


print(luhn(cc_num))
