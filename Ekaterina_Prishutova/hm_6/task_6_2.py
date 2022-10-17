from functools import reduce


def reducer_func(el_prev, el):
    if el_prev[-1] == el:
        return el_prev + "2"
    elif el_prev[-1].isdigit() and el_prev[-2] == el:
        return el_prev[:-1] + str(int(el_prev[-1]) + 1)
    else:
        return el_prev + el


print(reduce(reducer_func, 'aaabbdefffff'))
