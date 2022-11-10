from func import Methods


class Calculate(Methods):

    def addition(self, num_1, num_2):
        assert isinstance(num_1, (float, int)), 'Numbers can be int or float!'
        assert isinstance(num_2, (float, int)), 'Numbers can be int or float!'
        return num_1 + num_2

    def subtraction(self, num_1, num_2):
        assert isinstance(num_1, (float, int)), 'Numbers can be int or float!'
        assert isinstance(num_2, (float, int)), 'Numbers can be int or float!'
        return num_1 - num_2

    def multiplication(self, num_1, num_2):
        assert isinstance(num_1, (float, int)), 'Numbers can be int or float!'
        assert isinstance(num_2, (float, int)), 'Numbers can be int or float!'
        return num_1 * num_2

    def division(self, num_1, num_2):
        assert isinstance(num_1, (float, int)), 'Numbers can be int or float!'
        assert isinstance(num_2, (float, int)), 'Numbers can be int or float!'
        assert num_2 != 0, 'Division by zero!'
        return num_1 / num_2


calculator = Calculate()

print(calculator.addition(1, 2))
print(calculator.subtraction(3, 4))
print(calculator.multiplication(5, 6))
print(calculator.division(7, 8))

print(calculator.addition('a', 2))
print(calculator.division(7, 0))
