def words_len_list(sample_text):
    sample_text = [len(word) for word in sample_text.split() if word != 'the']
    return sample_text


sentence = 'thequick brown fox jumps over the lazy dog'
print(words_len_list(sentence))
