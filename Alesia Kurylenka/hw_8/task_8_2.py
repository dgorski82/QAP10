number_names = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
}


def decorator(func):
    def wrapper(*args):
        list_values = []
        for k, v in number_names.items():
            for arg in args:
                if arg == k:
                    list_values.append(v)
                    list_values = sorted(list_values)
        list_2 = []
        for value in list_values:
            for k, v in number_names.items():
                if value == v:
                    list_2.append(k)
        func(*list_2)
    return wrapper


@decorator
def print_numbers(*args):
    print(*args)


print_numbers(1, 2, 3)
print_numbers(1, 2, 3, 4, 19, 8)
