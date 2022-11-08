from func import Methods


class Calculator(Methods):

    @staticmethod
    def validation(number1, number2):
        assert type(number1) == int or type(number1) == float, "Enter integer or float number"
        assert type(number2) == int or type(number2) == float, "Enter integer or float number"

    def addition(self, number1, number2):
        self.validation(number1, number2)
        print(f"Your addition result: {number1 + number2}")

    def subtraction(self, number1, number2):
        self.validation(number1, number2)
        print(f"Your subtraction result: {number1 - number2}")

    def multiplication(self, number1, number2):
        self.validation(number1, number2)
        print(f"Your multiplication result: {number1 * number2}")

    def division(self, number1, number2):
        self.validation(number1, number2)
        if int(number2) == 0:
            raise ZeroDivisionError("Please enter number not equal to zero")
        print(f"Your division result: {number1 / number2}")


calc = Calculator()
calc.addition(20, 13)
calc.division(20, 4.5)
calc.subtraction(5, 3.3)
calc.multiplication(2.2, 8)
