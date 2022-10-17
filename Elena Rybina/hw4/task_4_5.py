a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
c = {**a, **b}
print(c)
for k in c.keys():
    c[k] = [a.get(k), b.get(k)]
print(c)
