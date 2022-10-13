def init_constant(lang: str) -> dict:
    if lang == 'eng':
        upper_letter, lower_letter = 'A', 'a'
        amount_letter = 26
    else:
        upper_letter, lower_letter = 'А', 'а'
        amount_letter = 32

    return {'l': lang,
            'ul': upper_letter,
            'll': lower_letter,
            'al': amount_letter}


def cesar_coding(in_str: str, bias: int, lang: str) -> str:
    assert lang in ('eng', 'rus'), 'You can use only ENG|RUS language'

    init = init_constant(lang)

    out_string = str()
    for i in in_str:
        if i.isupper():
            out_string += chr((ord(i) - ord(init.get('ul')) + bias) % init.get('al') + ord(init.get('ul')))
        elif i.islower():
            out_string += chr((ord(i) - ord(init.get('ll')) + bias) % init.get('al') + ord(init.get('ll')))
        elif i.isdigit():
            out_string += str((int(i) + bias) % 10)
        else:
            out_string += i
    return out_string


print(cesar_coding('Hello World!', 4, 'eng'))
print(cesar_coding('Привет Мир!', 4, 'rus'))


def cesar_decoding(in_str: str, bias: int, lang='eng') -> str:
    assert lang in ('eng', 'rus'), 'You can use only ENG|RUS language'

    init = init_constant(lang)

    out_string = str()
    for i in in_str:
        if i.isupper():
            out_string += chr((ord(i) - ord(init.get('ul')) - bias) % init.get('al') + ord(init.get('ul')))
        elif i.islower():
            out_string += chr((ord(i) - ord(init.get('ll')) + bias) % init.get('al') + ord(init.get('ll')))
        elif i.isdigit():
            out_string += str((int(i) - bias) % 10)
        else:
            out_string += i
    return out_string


print(cesar_decoding('Lipps Asvph!', 4, 'eng'))
print(cesar_decoding('Уфмжйц Рмф!', 4, 'rus'))


# Try make Two-in-one using OOP

class CesarCodeDecode:

    def __init__(self, str_in, bias):
        self.str_in = str_in
        self.bias = bias

    @staticmethod
    def install_vars(lang) -> tuple:
        if lang == 'eng':
            upper, lower = 'A', 'a'
            amount = 26
        else:
            upper, lower = 'А', 'а'
            amount = 32
        return upper, lower, amount

    def coding(self, lang):
        assert lang in ('eng', 'rus'), 'You can use only ENG|RUS language'

        upper, lower, amount = self.install_vars(lang)

        out_string = str()
        for i in self.str_in:
            if i.isupper():
                out_string += chr((ord(i) - ord(upper) + self.bias) % amount + ord(upper))
            elif i.islower():
                out_string += chr((ord(i) - ord(lower) + self.bias) % amount + ord(lower))
            elif i.isdigit():
                out_string += str((int(i) + self.bias) % 10)
            else:
                out_string += i
        return out_string

    def decoding(self, lang):
        self.bias = - self.bias
        out_string = self.coding(lang)
        return out_string


print(CesarCodeDecode('Hello World!', 4).coding('eng'))
print(CesarCodeDecode('Привет Мир!', 4).coding('rus'))
print(CesarCodeDecode('Lipps Asvph!', 4).decoding('eng'))
print(CesarCodeDecode('Уфмжйц Рмф!', 4).decoding('rus'))
