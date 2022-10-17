list_names = ['Ann', 'Alex', 'Mark', 'Max']
len_list_names = len(list_names)
if len_list_names == 0:
    print('No one likes this')
elif len_list_names == 1:
    print(f'{list_names[0]} likes this')
elif len_list_names == 2:
    print(f'{list_names[0]} and {list_names[1]} likes this')
elif len_list_names == 3:
    print(f'{list_names[0]}, {list_names[1]} and {list_names[2]} likes this')
else:
    print(f'{list_names[0]}, {list_names[1]} and 2 others like this')
