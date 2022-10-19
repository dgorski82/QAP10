import collections
string = input("Please, insert letters:   ")


def calculate(letters):
    calculate_dict = dict(collections.Counter(letters))
    strings = []
    for key, value in calculate_dict.items():
        if value == 1:
            strings.append(str(key))
        else:
            strings.append(f"{key}{value}")
    calculated_letters = "".join(strings)

    return calculated_letters


print(calculate(string))
