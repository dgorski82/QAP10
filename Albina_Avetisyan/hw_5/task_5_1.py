likes = ['Pol', 'Ron', 'Ana', 'Nik', 'Garold']
if len(likes) == 1:
    print(likes[0], "likes this")
elif len(likes) == 2:
    print(likes[0], "and", likes[1], "like this")
elif len(likes) == 3:
    print(likes[0], likes[1], "and", likes[2], "like this")
elif len(likes) >= 4:
    print(likes[0], likes[1], "and", len(likes) - 2, "others like this")
else:
    print("No one likes this")
