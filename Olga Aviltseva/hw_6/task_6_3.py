def calculator(operation, a, b):

    if operation == 1:
        return a + b
    elif operation == 2:
        return a - b
    elif operation == 3:
        return a * b
    elif operation == 4:
        if b == 0:
            return "Can't divide by zero"
        else:
            return a / b
    else:
        return "Please ran the program again"


operation = input("Select an action: 1 - Addition, 2 - Subtraction, 3 - Multiplication, 4 - Division ")
a = input("Enter the first number: ")
b = input("Enter the second number: ")

print(calculator(int(operation), float(a), float(b)))
