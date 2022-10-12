a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
c = a | b

print(c.keys())
for k, v in a.items():
    for kk, vv in b.items():
        c[k] = [a.get(k), b.get(k)]

for k, v in b.items():
    for kk, vv in a.items():
        c[k] = [a.get(k), b.get(k)]
print(c)
