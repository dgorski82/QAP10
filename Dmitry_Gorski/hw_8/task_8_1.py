from functools import wraps


def typed(type_in):
    assert type_in in ('str', 'int', 'float'), 'Only (int, str, float) type you can use'

    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            return func(*list(map(getattr(__builtins__, type_in), args)))

        return wrapper

    return decorator


@typed(type_in='float')
def test_function(*args):
    """
    func for addition input data
    :param args:  int, float, str
    :return: int, float, str
    """
    try:
        return sum([*args])
    except TypeError:
        return ''.join([*args])


print(test_function(10, 20., 30))
