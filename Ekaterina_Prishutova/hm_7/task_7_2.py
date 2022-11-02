numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

generator_list = [number for number in numbers if number > 0]
print(generator_list)
generator_list_2 = [abs(number) for number in numbers]
print(generator_list_2)
