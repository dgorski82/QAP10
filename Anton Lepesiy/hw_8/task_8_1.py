def typed_func(type):
    def wrapper(function):
        def wrap(*args):
            new_list = []
            if type == 'str':
                for element in args:
                    new_list.append(str(element))
            elif type == 'int':
                for element in args:
                    new_list.append(int(element))
            elif type == 'float':
                for element in args:
                    new_list.append(float(element))
            return function(*new_list)
        return wrap
    return wrapper


@typed_func(type='str')
def add_two_symbols(a, b):
    return a + b


print('typed func: add_two_symbols:')
print(add_two_symbols("3", 5))
print(add_two_symbols(5, 5))
print(add_two_symbols('a', 'b'))


print('typed func: add_three_symbols:')


@typed_func(type='int')
def add_three_symbols(a, b, c):
    return a + b + c


print(add_three_symbols(5, 6, 7))
print(add_three_symbols("3", 5, 0))


@typed_func(type='float')
def add_three_symbols(a, b, c):
    return a + b + c


print(add_three_symbols(0.1, 0.2, 0.4))
