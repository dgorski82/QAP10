from num2words import num2words


def sort_numbers(func):
    def wrapper(*args):
        d = {}
        if len(args) < 100:
            for num in args:
                if 0 < num < 19:
                    d[num] = num2words(num)
                else:
                    print("The entered number should be greater than 0 and less than 19")
        else:
            print("The max number of entered numbers should not exceed 100")
        func(list(dict(sorted(d.items(), key=lambda item: item[1])).keys()))

    return wrapper


@sort_numbers
def print_sort_numbers(*args):
    print(args)


print_sort_numbers(0, 5, 11, 4, 1, 2, 3)
