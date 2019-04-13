secret = 2
guess = 0

while True:
    guess = int(input("Guess the secret number: "))

    if guess == secret:
        print("Congrats. The secret number is 2!")
        break

    else:
        print("Incorrect. The secret number is not " + str(guess))









