likes = ("Ann", "Alex", "Mark", "Max")

a = len(likes)


if likes == 0:
    print("no one likes this.")
elif type(likes) == str:
    print('Колличество лайков: 1')
    print(f" {likes} like this.")
elif a == 2:
    print('Колличество лайков: ', a)
    print(" and ".join(likes), "like this.")
elif a == 3:
    print('Колличество лайков: ', a)
    print(likes[0], ',', likes[1], "and", likes[2], 'like this.')
elif a >= 4:
    print('Колличество лайков: ', a)
    print(likes[0], ',', likes[1], 'and 2 others like this.')
