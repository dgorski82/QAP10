array = [1, 5, 2, 9, 2, 9, 1]  # не повторяется 5
array_2 = [4, 11, 15, 7, 11, 8, 15, 7, 11, 8]  # не повторяется 4


def findUnique(list):
    dup = [x for i, x in enumerate(list) if i != list.index(x)]
    for i in list:
        if i not in dup:
            print(i)


findUnique(array)
findUnique(array_2)
