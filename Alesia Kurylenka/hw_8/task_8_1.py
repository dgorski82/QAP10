def typed(type):
    def wrapper(func):
        def wrapper_1(*args):
            new_list = []
            if type == 'str':
                for i in args:
                    new_list.append(str(i))
            elif type == 'int':
                for i in args:
                    new_list.append(float(i))
            return func(*new_list)
        return wrapper_1
    return wrapper


@typed(type='str')
def add_two_symbols(a, b):
    return a + b


@typed(type='int')
def add_three_symbols(a, b, с):
    return a + b + с


print(add_two_symbols("3", 5))
print(add_two_symbols(5, 5))
print(add_two_symbols('a', 'b'))

print(add_three_symbols(5, 6, 7))
print(add_three_symbols("3", 5, 0))
print(add_three_symbols(0.1, 0.2, 0.4))
