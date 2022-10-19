def reshape(lst, el1, el2):
    lst = iter(lst)
    new = []
    for _ in range(el1):
        elem = []
        for _ in range(el2):
            elem.append(next(lst))
        new.append(elem)
    print(new)


reshape([1, 2, 3, 4, 5, 6], 2, 3)

reshape([1, 2, 3, 4, 5, 6, 7, 8], 4, 2)
