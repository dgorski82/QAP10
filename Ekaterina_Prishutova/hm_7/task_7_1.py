def func_var_1(input_list, length, width):
    assert len(input_list) is length * width, "Неверно заданы размеры"
    list_1 = [[] for i in range(width)]
    [list_1[int(value[0] / length)].append(value[1]) for value in enumerate(input_list)]
    return list_1


def func_var_2(input_list, length, width):
    assert len(input_list) is length * width, "Неверно заданы размеры"
    return [input_list[i:i + length] for i in range(0, len(input_list), length)]


print(func_var_1([1, 2, 3, 4, 5, 6], 3, 2))
print(func_var_2([1, 2, 3, 4, 5, 6], 2, 3))
