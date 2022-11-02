import random

secret_number = str(random.randint(1000, 9999))
print("Guess the number. It contains 4 digits.")

while True:
    cows = 0
    bulls = 0

    player_guess = input("Enter your guess: ")

    if len(player_guess) != 4:
        print('Incorrect input!')
        break

    else:

        if player_guess[0] == secret_number[0]:
            bulls += 1
        if player_guess[1] == secret_number[1]:
            bulls += 1
        if player_guess[0] == secret_number[1]:
            cows += 1
        if player_guess[1] == secret_number[0]:
            cows += 1

        print("Bulls: ", bulls)
        print("Cows: ", cows)

        if bulls == 4:
            print('Yay, You Won!')
