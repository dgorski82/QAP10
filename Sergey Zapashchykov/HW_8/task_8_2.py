number_names = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
                9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
                16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}


def decor(func):
    def wrapper(*args):
        args = sorted(list(args), key=lambda number: number_names[number])
        func(*args)
    return wrapper


@decor
def numbers(*args):
    print(*args)


numbers(1, 2, 3)
