from func import Methods


class Calculator(Methods):

    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Деление на ноль запрещено."


calc = Calculator()
print(calc.multiplication(1, 2))
print(calc.division(1, 0))
print(calc.addition(1, 2))
print(calc.subtraction(1, 2))
