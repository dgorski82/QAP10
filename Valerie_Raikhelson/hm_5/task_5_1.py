from langdetect import detect
from translate import Translator

target_lang = 'en'
names = []

for _ in range(2):
    name = input("Enter name: ")
    names.append(name)

if len(names) > 0:
    result_lang = detect(names[0])

if result_lang == target_lang:

    if len(names) == 0:
        print("no one likes this")
    if len(names) == 1:
        print(names[0], "likes this")
    if len(names) == 2:
        print(names[0], "and", names[1], "like this")
    if len(names) == 3:
        print(names[0], names[1], "and", names[2], "like this")
    if len(names) == 4:
        print(names[0], names[1], "and two others like this")
else:
    translator = Translator(result_lang)
    if len(names) == 0:
        print("no one likes this")
    if len(names) == 1:
        print(names[0], translator.translate("likes this"))
    if len(names) == 2:
        print(names[0], translator.translate("and"), names[1], translator.translate("like this"))
    if len(names) == 3:
        print(names[0], names[1], translator.translate("and"), names[2], translator.translate("like this"))
    if len(names) == 4:
        print(names[0], names[1], translator.translate("and two others like this"))
