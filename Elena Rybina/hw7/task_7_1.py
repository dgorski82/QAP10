def reshape(list_1, num_1, num_2):
    list_1 = iter(list_1)
    new_list = []
    for _ in range(num_1):
        elem = []
        for _ in range(num_2):
            elem.append(next(list_1))
        new_list.append(elem)
    print(new_list)


reshape([1, 2, 3, 4, 5, 6], 2, 3)

reshape([1, 2, 3, 4, 5, 6, 7, 8], 4, 2)
