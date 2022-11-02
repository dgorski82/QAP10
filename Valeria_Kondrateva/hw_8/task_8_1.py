def typed(need_type):
    def decorator(func):
        def wrapper(*args):
            lst = []
            if need_type == 'str':
                for i in args:
                    lst.append(str(i))
                return func(*lst)
            elif need_type == 'int':
                for i in args:
                    lst.append(float(i))
                return func(*lst)

        return wrapper
    return decorator


@typed(need_type='str')
def add_two_symbols(a, b):
    return a + b


@typed(need_type='int')
def add_three_symbols(a, b, c):
    return a + b + c


print(add_two_symbols("3", 5))
print(add_two_symbols(5, 5))
print(add_two_symbols('a', 'b'))
print(add_three_symbols(5, 6, 7))
print(add_three_symbols("3", 5, 0))
print(add_three_symbols(0.1, 0.2, 0.4))
