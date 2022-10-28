import random
number_1 = ''.join(random.sample('12345678', 4))   # the secret number
print('HELP: the secret number is: ', number_1)
cows = 0
bulls = 0
while True:
    number_2 = input('Please enter four-digit number with non-repetitive digits: ')  # try to guess
    print('yor\'s number: ', number_2)

    if not len(number_2):
        print('Error! You are not entered number. Enter four-digit number!')

    elif number_2 == number_1:
        print('You won!')
        break

    elif len(number_2) != 4:
        print('Error! Your\'s number is not four-digit. Enter four-digit number!')

    elif len(set(number_2)) != len(number_1):
        print('Error! Your\'s number has repetitive digits')

    else:

        for i in list(number_1):
            for i2 in list(number_2):
                if i == i2:
                    cows += 1

        if number_1[0] == number_2[0]:
            bulls += 1
        if number_1[1] == number_2[1]:
            bulls += 1
        if number_1[2] == number_2[2]:
            bulls += 1
        if number_1[3] == number_2[3]:
            bulls += 1

        print("cows: ", cows)
        print("bulls: ", bulls)
        bulls = 0
        cows = 0
