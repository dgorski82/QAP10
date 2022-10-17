import string

alfavit = string.ascii_letters
alfavit_rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
number = 3
string_1 = "heLLo world, прИвет мир!"
string_3 = "khOOr zruog, туЛезх плу!"


def encode(string_1):
    string_2 = ""
    for i in string_1:
        if i in alfavit:
            string_2 = string_2 + alfavit[int(alfavit.index(i)) + number]
        elif i in alfavit_rus:
            string_2 = string_2 + alfavit_rus[int(alfavit_rus.index(i)) + number]
        else:
            string_2 = string_2 + i
    return string_2


print(encode(string_1))


def decode(string_3):
    string_4 = ""
    for i in string_3:
        if i in alfavit:
            string_4 = string_4 + alfavit[int(alfavit.index(i)) - number]
        elif i in alfavit_rus:
            string_4 = string_4 + alfavit_rus[int(alfavit_rus.index(i)) - number]
        else:
            string_4 = string_4 + i
    return string_4


print(decode(string_3))
