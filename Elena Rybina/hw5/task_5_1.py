names = ['Peter', 'Ann', 'Alex', 'Mark']
likes = len(names)
if likes == 0:
    print('No one likes this')
elif likes == 1:
    print(f'{names[0]} likes this')
elif likes == 2:
    print(f'{names[0]} and {names[1]} likes this')
elif likes == 3:
    print(f'{names[0]}, {names[1]} and {names[2]} likes this')
else:
    print(f'{names[0]}, {names[1]} and {len(names) - 2} others like this')
