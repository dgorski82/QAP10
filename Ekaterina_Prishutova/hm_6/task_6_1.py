def validate(number):
    x_origin = []
    if len(number) == 0:
        return "Invalid input parameters"
    for i in number:
        if not i.isdigit():
            return "Invalid input parameters"
        x_origin.append(int(i))
    sum_1 = sum(x_origin[-1::-2]) + sum(list(map(lambda x: int(x * 2 / 10) + x * 2 % 10, x_origin[-2::-2])))
    return "Valid" if sum_1 % 10 == 0 else "Not valid"


print(validate("4561261212345467"))
