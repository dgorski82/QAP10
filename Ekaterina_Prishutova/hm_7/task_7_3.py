words = "thequick brown fox jumps over the lazy dog"

generator_list = [len(word) for word in words.split(" ") if word != "the"]
print(generator_list)
