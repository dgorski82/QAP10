import random


def insert_num():
    while True:
        num = input("number: ")
        set_hidden_num = set(map(int, num))
        if len(set_hidden_num) == 4:
            break
    return set_hidden_num


def get_random_num():
    set_random_num = set()
    for _ in range(10):
        set_random_num.add(random.randint(1, 9))
        if len(set_random_num) == 4:
            break
    return set_random_num


list_hid_num = list(insert_num())
list_ran_num = list(get_random_num())
print(list_hid_num)
print(list_ran_num)

for i in list_hid_num:
    for k in list_ran_num:
        if i == k:
            if list_hid_num.index(i) == list_ran_num.index(k):
                print(i, "бык")
            else:
                print(i, "корова")
