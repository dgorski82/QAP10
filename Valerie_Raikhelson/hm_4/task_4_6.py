from collections import Counter

numbers = [1, 5, 5, 2, 9, 2, 9, 1]
el_count = Counter(numbers)

print(el_count)
for num, count in el_count.items():
    if count == min(el_count.values()):
        if count == 1:
            print(num)
