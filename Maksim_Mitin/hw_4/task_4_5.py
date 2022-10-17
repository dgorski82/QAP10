a = {"a": 1, "b": 2, "c": 3}
b = {"c": 3, "d": 4, "e": 5}
ab = a | b

for k, v in b.items():
    if a.get(k):
        ab[k] = [a[k], v]
    else:
        ab[k] = [None, v]

for k, v in a.items():
    if b.get(k):
        ab[k] = [b[k], v]
    else:
        ab[k] = [v, None]

print(ab)

#  d = {}      - ещё вот такой более продвинутый способ попробовал сделать, вроде работает так как надо
# for elem in list(a.keys()) + list(b.keys()):
#    d[elem] = ([a.get(elem, ), b.get(elem, )])
# print(d)
