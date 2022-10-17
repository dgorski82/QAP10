import collections
string = input("Введите строку ")


def count(letters):
    count_dict = dict(collections.Counter(letters))
    strings = []
    for key, value in count_dict.items():
        if value == 1:
            strings.append("{}{}".format(key, ""))
        else:
            strings.append("{}{}".format(key, value))
    result = "".join(strings)

    return result


print(count(string))
