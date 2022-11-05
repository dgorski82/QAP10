number_names = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
                5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
                10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
                15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}


def lexografic_sorter(func):
    def wrapper(*args):
        print('inserted numbers:', *args)
        list_of_numbers_names = []
        for arg in args:
            for key, value in number_names.items():
                if key == arg:
                    list_of_numbers_names.append(value)
        sorted_number_names = sorted(list_of_numbers_names)
        list_of_sorted_numbers = []
        for name in sorted_number_names:
            for key, value in number_names.items():
                if value == name:
                    list_of_sorted_numbers.append(key)
        func(list_of_sorted_numbers)
    return wrapper


@lexografic_sorter
def numbers_ptinter(*args):

    print('lexografic sorted numbers:', *args)


numbers_ptinter(1, 2, 3)
numbers_ptinter(1, 5, 15, 9)
