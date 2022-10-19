sentence = " thequick brown fox jumps over the lazy dog"
list_of_word_lengths = []
[list_of_word_lengths.append(len(word)) for word in sentence.replace("the", "").split(" ") if len(word) > 0]
print(list_of_word_lengths)
