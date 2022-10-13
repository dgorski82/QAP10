import numpy as np


def reshape_v1(lst: list, length: int, width: int) -> list:
    out_lst = []
    assert len(lst) == length * width, \
        "Выходной массив не может быть сформирован"

    for i in range(length):
        out_lst.append([lst[x] for x in range(width * i, (width * i + width))])
    return out_lst


print(reshape_v1([1, 2, 3, 4, 5, 6, 7, 8], 4, 2))
print(reshape_v1([1, 2, 3, 4, 5, 6], 2, 3))


def reshape_v2(some_list: list, length: int, width: int) -> np.array:
    return np.array(some_list).reshape(length, width)


print(reshape_v2([1, 2, 3, 4, 5, 6], 2, 3))
print(reshape_v2([1, 2, 3, 4, 5, 6, 7, 8], 4, 2))
