def typed(type):
    def decorator(func):
        def wrapper(*args):
            if type == 'str':
                func(''.join(convert_args(str, args)))
            elif type == 'int':
                func(sum(convert_args(int, args)))
            elif type == 'float':
                func(sum(convert_args(float, args)))

        return wrapper

    return decorator


def convert_args(type, args):
    return map(type, args)


@typed(type='str')
def add_two_symbols(*args):
    print(args)


@typed(type='int')
def add_three_symbols(*args):
    print(args)


@typed(type='float')
def add_four_symbols(*args):
    print(args)


add_two_symbols("3", "a")
add_three_symbols(1, "2")
add_four_symbols(0.1, 0.2, 0.4, 0.7)
