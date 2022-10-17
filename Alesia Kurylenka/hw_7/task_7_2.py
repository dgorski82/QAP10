numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
generator_1 = [abs(number) for number in numbers]
print(generator_1)

string = " thequick brown fox jumps over the lazy dog"
generator_2 = [len(i) for i in string.split() if i != 'the']
print(generator_2)
