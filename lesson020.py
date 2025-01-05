import random
answer = random.randint(1, 100)

guess = int(input("Enter an integer from 1 to 100: "))


while guess != answer:
    while guess > 100 or guess < 1:
        print("Invalid number")
        guess = int(input("Enter an integer from 1 to 100: "))

    if guess > answer:
        print("Too high!")
    elif guess < answer:
        print("Too low!")

    guess = int(input("Enter an integer from 1 to 100: "))

print("You guessed it!")