list_names = input("Enter names")
likes = len(list_names.split())
names = (list_names.split(", "))


if likes == 0:
    print("No likes")
elif likes == 1:
    print(names[0] + " likes this")
elif likes == 2:
    print(names[0], "and " + names[1], " likes this")
elif likes == 3:
    print(names[0], ", " + names[1], "and " + names[2], " likes this")
else:
    print(names[0], ", " + names[1], "and ", likes - 2, "others like this")
