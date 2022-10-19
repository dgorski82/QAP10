num_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
            9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
            16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}


def sorted_tool(func):
    def wrapper(*args):
        if all(isinstance(arg, int) for arg in args):
            if all(0 <= arg < 20 for arg in args):
                if len(args) <= 100:
                    return func(*args)
                return 'The total number of args must not gt 100'
            return 'All args must be in range [0; 20)'
        return 'All args must be int'
    return wrapper


@sorted_tool
def lexicographic_sort(*args):
    return list(dict(sorted([(v, k) for k, v in
                             {k: v for k, v in num_dict.items() for arg in args if arg == k}.items()])).values())
