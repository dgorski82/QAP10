import operator


def input_number():
    return float(input("Введите число:\n"))


def select_operation():
    return input("Выберите операцию:\n"
                 "+, -, *, /, **, = \n")


def get_math_expression():
    operation = ''
    math_expression = []
    while operation != "=":
        math_expression.append(input_number())
        operation = select_operation()
        math_expression.append(operation)
    return math_expression


def replace_with_intermediate_result(math_expression, index_of_operation, intermediate_result):
    math_expression[index_of_operation - 1] = intermediate_result
    math_expression.pop(index_of_operation + 1)
    math_expression.pop(index_of_operation)
    print(math_expression)


def calculate():
    math_expression = get_math_expression()
    while len(math_expression) > 2:
        if "**" in math_expression:
            index_of_operation = math_expression.index("**")
            result = math_expression[index_of_operation - 1] ** math_expression[index_of_operation + 1]
            replace_with_intermediate_result(math_expression, index_of_operation, result)
            continue
        if "*" in math_expression:
            index_of_operation = math_expression.index("*")
            result = math_expression[index_of_operation - 1] * math_expression[index_of_operation + 1]
            replace_with_intermediate_result(math_expression, index_of_operation, result)
            continue
        if "/" in math_expression:
            index_of_operation = math_expression.index("/")
            assert math_expression[index_of_operation + 1] != 0, 'Divisor cannot be zero'
            result = math_expression[index_of_operation - 1] / math_expression[index_of_operation + 1]
            replace_with_intermediate_result(math_expression, index_of_operation, result)
            continue
        if "+" in math_expression:
            index_of_operation = math_expression.index("+")
            result = math_expression[index_of_operation - 1] + math_expression[index_of_operation + 1]
            replace_with_intermediate_result(math_expression, index_of_operation, result)
            continue
        if "-" in math_expression:
            index_of_operation = math_expression.index("-")
            result = math_expression[index_of_operation - 1] - math_expression[index_of_operation + 1]
            replace_with_intermediate_result(math_expression, index_of_operation, result)
            continue
    print(result)


calculate()
