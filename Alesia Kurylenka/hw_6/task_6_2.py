from collections import Counter


def letter_count(string1):
    string2 = ""
    for key, value in Counter(string1).items():
        if value == 1:
            string2 += f"{key}"
        else:
            string2 += f'{key}{value}'
    return string2


string1 = "aaabbdefffff"
print(letter_count(string1))
