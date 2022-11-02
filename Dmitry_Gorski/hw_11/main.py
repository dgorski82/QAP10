from functools import reduce
from func import Methods, Operation


class Calculator(Methods):

    @staticmethod
    def check_args(*args, **kwargs):
        assert ''.join(kwargs.values()) in Operation.keys(),\
            f'Only {",".join(Operation.keys())} can be used'
        assert all(isinstance(arg, (int, float)) for arg in args),\
            'Only int|float input type can be used'

    def calculate(self, *args, **kwargs):
        self.check_args(*args, **kwargs)
        try:
            return reduce(getattr(float, Operation.get("".join(kwargs.values()))), map(float, args))
        except ZeroDivisionError:
            return "You can't divide by zero!"


calc = Calculator()

# valid case
print(calc.calculate(1, 2, 3, mode='+'))
print(calc.calculate(1, .2, 3, mode='-'))
print(calc.calculate(1, 19.12, 3, mode='/'))
print(calc.calculate(1, 2., 3, mode='*'))

# case divide by zero
print(calc.calculate(1, 0, 3, mode='/'))

# assert case
print(calc.calculate(1, '2', 3, mode='*'))
print(calc.calculate(1, 2, 3, mode='&'))
