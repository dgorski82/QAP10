def count_letters(instr):
    instr_space = instr + " "
    result = ""
    same_letters_cnt = 1
    strlen = len(instr_space)

    if strlen < 2:
        return instr

    for index in range(strlen - 1):
        if instr_space[index] == instr_space[index + 1]:
            same_letters_cnt += 1
        else:
            result += instr_space[index]
            if same_letters_cnt > 1:
                result = result + str(same_letters_cnt)
                same_letters_cnt = 1

    return result


print(count_letters("cccbba"))
print(count_letters("abeehhhhhccced"))
print(count_letters("aaabbceedd"))
print(count_letters("abcde"))
print(count_letters("aaabbdefffff"))
