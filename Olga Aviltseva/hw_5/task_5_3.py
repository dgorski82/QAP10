from random import randint

number_to_guess = []
cows = 0
bulls = 0

while len(number_to_guess) < 4:
    number = randint(0, 9)
    if number not in number_to_guess:
        number_to_guess.append(number)

validation_result = True

while bulls != 4:
    user_guess = input("Please guess 4-digit number: ")

    if user_guess == "q":
        break

    validation_result = len(user_guess) == 4

    if validation_result:
        validation_result = user_guess.isdigit()

    if validation_result:
        sorted_user_guess = sorted(user_guess)

        for index in range(0, len(user_guess) - 2):
            validation_result = sorted_user_guess[index] != sorted_user_guess[index + 1]
            if not validation_result:
                break

    if not validation_result:
        print("Incorrect input")
        continue

    cows = 0
    bulls = 0
    for index in range(0, len(user_guess)):

        if int(user_guess[index]) == number_to_guess[index]:
            bulls += 1
        elif int(user_guess[index]) in number_to_guess:
            cows += 1

    print(bulls, "bulls ", cows, "cows")
    if bulls == 4:
        print("You win!!!")
