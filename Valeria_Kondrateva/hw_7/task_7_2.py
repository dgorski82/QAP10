def divide(numbers):
    positive = []
    for i in numbers:
        if i > 0:
            positive.append(i)
    return positive


nums = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
pos = divide(nums)
print(pos)
