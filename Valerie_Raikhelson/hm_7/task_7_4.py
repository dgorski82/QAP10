import string
from langdetect import detect
from translate import Translator

alphabet_uppercase = string.ascii_uppercase
alphabet_lowercase = string.ascii_lowercase


def replace_letter(list, step, alphabet_upper, alphabet_lower):
    for i in range(len(list)):
        if list[i].isalpha():
            if list[i].isupper():
                list[i] = alphabet_upper[alphabet_upper.find(list[i]) + step]
            else:
                list[i] = alphabet_lower[alphabet_lower.find(list[i]) + step]
    return list


def encrypt(step, sentence):
    result_lang = detect(sentence)
    list_of_sent = list(sentence)
    if result_lang == 'en':
        replace_letter(list_of_sent, step, alphabet_uppercase, alphabet_lowercase)
    else:
        translator = Translator(result_lang)
        alphabet_uppercase_any_lang = translator.translate(alphabet_uppercase).replace(
            "All of the letters of the alphabet, lowercase", "")
        alphabet_lowercase_any_lang = translator.translate(alphabet_lowercase).replace(
            alphabet_lowercase, "")
        replace_letter(list_of_sent, step, alphabet_uppercase_any_lang, alphabet_lowercase_any_lang)
    return ' '.join(list_of_sent)


print(encrypt(1, "hello world!"))


def my_cipher(sentence):
    return sentence[::-1]


print(my_cipher("hello"))
