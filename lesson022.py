import random

secretNumber = random.randint(1, 10)

maxAttempts = 3

while maxAttempts > 0:
    guess = int(input("Guess the secret number: "))
    if guess == secretNumber:
        print(f"Yes it is {guess}")
        break
    elif guess > secretNumber:
        print("Too high!")
    elif guess < secretNumber:
        print("Too low!")
    maxAttempts -= 1

if maxAttempts == 0:
    print("You lost.")

