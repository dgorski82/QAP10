def calculation():
    user_input = input("Please choose the program and enter: \nfor Addition - add, \n"
                       "for Subtraction - sub, \nfor Multiplication - mul, \nfor Division - div: "
                       "\nfor math_expression - exp: ")
    assert user_input in ["add", 'sub', 'mul', 'div', 'exp'], "Enter valid operation"
    if user_input in ["add", 'sub', 'mul', 'div']:
        number1 = input("Please enter first number: ")
        number2 = input("Please enter second number: ")
        assert number1.isdigit() and number2.isdigit(), "please enter digits only"
        number1 = float(number1)
        number2 = float(number2)
        if user_input == "add":
            print(number1 + number2)
        elif user_input == "sub":
            print(number1 - number2)
        elif user_input == "mul":
            print(number1 * number2)
        elif user_input == "div":
            assert number2 != 0, "division by 0 is not allowed"
            int_part = int(number1 // number2)
            remainder = int(number1 % number2)
            print(f"integer part of number: {int_part}, remainder of division: {remainder}")
    elif user_input == 'exp':
        math_expression = input("Please enter your mathematical expression: ")
        if math_expression.isdigit() or math_expression not in ['-', '+', '*', '/', '**', '%', '//']:
            print("please enter valid mathematical expression")
        else:
            print(eval(math_expression))


calculation()
