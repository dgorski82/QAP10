string = "Hello world"

characters = [
    "q",
    "w",
    "e",
    "r",
    "t",
    "y",
    "u",
    "i",
    "o",
    "p",
    "a",
    "s",
    "d",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    "z",
    "x",
    "c",
    "v",
    "b",
    "n",
    "m",
]


def findCharacters(some_string):
    some_string.lower()
    text = some_string.replace(" ", "")
    dict = {}
    for t in text:
        if t in characters:
            dict[t] = text.count(t)
    m = max(dict.values())
    cont = m
    array = []
    for key in dict:
        if dict[key] == cont:
            array.append(key)
    print(array)


findCharacters(string)
