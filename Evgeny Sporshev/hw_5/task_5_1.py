likes_list = ['Ann', 'Bann', 'Cann', 'Dann']

if len(likes_list) == 0:
    print('No one likes this')
elif len(likes_list[0]) == len(likes_list[0].encode()):
    if len(likes_list) == 1:
        print(likes_list[0], 'likes this')
    elif len(likes_list) == 2:
        print(f'{likes_list[0]} and {likes_list[1]} like this')
    elif len(likes_list) == 3:
        print(f'{likes_list[0]}, {likes_list[1]} and {likes_list[2]} like this')
    else:
        print(f'{likes_list[0]}, {likes_list[1]} and {len(likes_list) - 2} others like this')
else:
    if len(likes_list) == 1:
        print(likes_list[0], 'любит это')
    elif len(likes_list) == 2:
        print(f'{likes_list[0]} и {likes_list[1]} любят это')
    elif len(likes_list) == 3:
        print(f'{likes_list[0]}, {likes_list[1]} и {likes_list[2]} любят это')
    else:
        print(f'{likes_list[0]}, {likes_list[1]} и {len(likes_list) - 2} других любят это')
