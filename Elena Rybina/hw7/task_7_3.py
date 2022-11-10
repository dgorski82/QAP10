lst = " thequick brown fox jumps over the lazy dog"
generator = [len(i) for i in lst.split() if i != 'the']
print(generator)
