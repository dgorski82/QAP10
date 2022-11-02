def sort(func):
    new_dict = {}
    for k in func:
        new_dict[func[k]] = k
    sorted_new_dict_keys = sorted(new_dict)

    result = {}
    for i in sorted_new_dict_keys:
        result[i] = new_dict[i]
    return result


number_names = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
                9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
                16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
print(sort(number_names))
