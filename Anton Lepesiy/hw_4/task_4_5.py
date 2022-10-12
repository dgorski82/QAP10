a = {'a': 1,
     'b': 2,
     'c': 3}
b = {'c': 3,
     'd': 4,
     'e': 5}


def concat(a, b):
    concat_keys = set(list(a.keys()) + list(b.keys()))
    concat_values = []

    for i in concat_keys:
        concat_values.append([a[i] if i in a else None, b[i] if i in b else None])

    concat_dict = dict(zip(concat_keys, concat_values))

    return concat_dict


print(concat(a, b))
