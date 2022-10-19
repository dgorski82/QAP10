def check_card(number_card, result=0):
    if all(x.isdigit() for x in number_card) and not len(number_card) == 0:
        created_list = list(map(int, number_card))

        for index, num in enumerate(created_list):

            if index % 2 == 0:
                memory = num * 2
                if memory > 9:
                    memory -= 9
                result += memory
            else:
                result += num

        return result % 10 == 0
    else:
        return "Incorrect input"


print(check_card('4561261212345464'))
print(check_card('4561261212345467'))
print(check_card('45612612 12345467'))
print(check_card('45612612A12345467'))
print(check_card(''))
