def generator(list_numbers):
    list_numbers = [number for number in list_numbers if number > 0]
    return list_numbers


numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
print(generator(numbers))
