def convert(symbol_type):
    def decorator(func_to_decor):
        def wrapper(*args):
            if symbol_type == 'str':
                return func_to_decor(*tuple(map(lambda x: str(x), args)))
            elif symbol_type == 'int':
                return func_to_decor(*tuple(map(lambda x: float(x), args)))
        return wrapper
    return decorator


@convert(symbol_type='str')
def add_two_symbols(a, b):
    return a + b


@convert(symbol_type='int')
def add_three_symbols(a, b, c):
    return a + b + c


print(add_two_symbols('3', 5))
print(add_two_symbols(5, 5))
print(add_two_symbols('a', 'b'))

print(add_three_symbols(5, 6, 7))
print(add_three_symbols("3", 5, 0))
print(add_three_symbols(0.1, 0.2, 0.4))
