alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
txt = input('Enter text to encrypt:  ').upper()


def encode(txt_1):
    step = int(input('Enter step to encrypt:'))
    place = ' '
    for i in txt_1.upper():
        place_now = alphabet.find(i)
        new_place = place_now + step
        if i in alphabet:
            place += alphabet[new_place]
        else:
            place += i
    return place


print(encode(txt))


txt_decode = input('Enter encrypted text: ').upper()


def decode(txt_1):
    step = int(input('Enter step to encrypt:'))
    place = ' '
    for i in txt_1.upper():
        place_now = alphabet.find(i)
        new_place = place_now - step
        if i in alphabet:
            place += alphabet[new_place]
        else:
            place += i
    return place


print(decode(txt_decode))
