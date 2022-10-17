bulls_and_cows = {}
number = 3219
list_number = [int(i) for i in str(number)]
print(list_number)

user_number = int(input('Enter 4 digit non-repeatable number: '))
while len(str(user_number)) != 4 or len(set(str(user_number))) < 4:
    print('Wrong number:')
    user_number = int(input('Enter 4 digit non-repeatable number: '))
list_user_number = [int(i) for i in str(user_number)]
print(list_user_number)

count_cows = 0
count_bulls = 0

for i in range(len(list_number)):
    if list_user_number[i] in list_number:
        count_cows += 1
    if list_user_number[i] == list_number[i]:
        count_bulls += 1
count_cows -= count_bulls
bulls_and_cows['cows'] = count_cows
bulls_and_cows['bulls'] = count_bulls

if count_bulls == 4:
    print('Your win!')
else:
    print(bulls_and_cows)
