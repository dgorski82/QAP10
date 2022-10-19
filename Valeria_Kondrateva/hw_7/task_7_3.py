def count(words):
    lst = words.split(' ')
    for i in range(len(lst)):
        if lst[i] == 'the':
            lst[i] = ''
    new_lst = []
    for i in lst:
        if len(i) != 0:
            new_lst.append(len(i))
    return new_lst


sentence = " thequick brown fox jumps over the lazy dog"

print(count(sentence))
