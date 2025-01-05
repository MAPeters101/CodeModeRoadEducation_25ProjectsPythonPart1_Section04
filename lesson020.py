import random
answer = random.randint(1, 100)

guess = int(input("Enter an integer from 1 to 100: "))

while guess > 100 or guess < 1:
    print("Invalid number")
    guess = int(input("Enter an integer from 1 to 100: "))



