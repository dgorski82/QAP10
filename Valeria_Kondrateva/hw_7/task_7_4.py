alf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
       'W', 'X', 'Y', 'Z']

text = "HELLO WORLDZ"
step = 1


def cesar(txt, stp):
    new_data = [(alf[(alf.index(i) + stp) % 26] if i != ' ' else ' ') for i in txt]
    result = ''.join(new_data)
    return result


def cesar2(txt, stp):
    new_data = [(alf[(alf.index(i) - stp) % 26] if i != ' ' else ' ') for i in txt]
    result = ''.join(new_data)
    return result


new_text = cesar(text, step)
print(new_text)

new_text = cesar2(new_text, step)
print(new_text)
