from collections import Counter

word = input("enter word:")

c = Counter(word)

result = []


def counting_number_of_letters():
    for k, v in c.items():
        if v == 1:
            result.append(k)
        if v > 1:
            result.append(k)
            result.append(str(v))
    return ''.join(result)


print(counting_number_of_letters())
