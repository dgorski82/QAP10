numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positive_numbers = [abs(number) if number < 0 else number for number in numbers]
print(positive_numbers)
