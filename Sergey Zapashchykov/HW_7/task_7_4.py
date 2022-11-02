def encode(encode_text: str, step: int):
    en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    encode_text_after = ''

    for letter in encode_text:
        if letter in en:
            letter_before = en.find(letter)
            if step >= 0:
                letter_after = letter_before + step
            else:
                letter_after = letter_before - abs(step)
            encode_text_after += en[letter_after]
        elif letter in ru:
            letter_before = ru.find(letter)
            if step >= 0:
                letter_after = letter_before + abs(step)
            else:
                letter_after = letter_before - step
            encode_text_after += ru[letter_after]
        else:
            encode_text_after += letter

    return encode_text_after


sample_1 = 'this is a test string'
sample_2 = 'hello world!'
sample_3 = 'ymnx nx f yjxy xywnsl'
sample_4 = 'khoor zruog!'
print(encode(sample_1, 5))
print(encode(sample_2, 3))
print(encode(sample_3, -5))
print(encode(sample_4, -3))
