choice = input(" Select an action:\n 1 - Addition\n 2 - Subtraction\n 3 - Multiplication\n "
               "4 - Division\nEnter Your choice: ")
a = input("Enter the first number: ")
b = input("Enter the second number: ")


def calculater(choice, a, b):
    if choice == 1:
        return a + b
    elif choice == 2:
        return a - b
    elif choice == 3:
        return a * b
    elif choice == 4:
        return a / b


print(calculater(int(choice), float(a), float(b)))
