def reshape(list_numbers, width, lenght):
    assert len(list_numbers) == width * lenght, 'Enter correct width and lenght!'

    list_numbers = iter(list_numbers)
    result_list = []

    for width_list in range(width):
        width_list = list()
        for _ in range(lenght):
            width_list.append(next(list_numbers))
        result_list.append(width_list)
    return result_list


print(reshape([1, 2, 3, 4, 5, 6], 2, 3))
print(reshape([1, 2, 3, 4, 5, 6, 7, 8], 4, 2))
