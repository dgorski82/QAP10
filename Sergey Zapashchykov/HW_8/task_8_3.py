def calculate():
    operator = input('Enter operation - addition, subtraction, multiplication, division or expression: ')
    if operator not in ['addition', 'subtraction', 'multiplication', 'division', 'expression']:
        return 'Enter correct operation!'
    if operator == 'expression':
        expression = input('Enter your expression: ')
        return eval(expression)
    number_1 = input('Enter your number 1: ')
    assert number_1.isdigit(), 'Enter number!'
    number_2 = input('Enter your number 2: ')
    assert number_2.isdigit(), 'Enter number!'
    if operator == 'addition':
        return int(number_1) + int(number_2)
    elif operator == 'subtraction':
        return int(number_1) - int(number_2)
    elif operator == 'multiplication':
        return int(number_1) * int(number_2)
    elif operator == 'division':
        assert int(number_2) != 0, 'Division by zero!'
        return int(number_1) / int(number_2)


print(calculate())
