#create your password variable and set it to a random password of your choosing
password = "I love Python!"
attempts = 5

guess = ""
#luckily for you, most of this code has already been written. Wrap this code around a while loop to ensure that it repeats until the amount of attempts are 0. Also, make sure to continue asking the user for their guess as the first statement in the while loop. Your job is to figure out what the proper condition in the while loop should be.
while attempts > 0:
  guess = input("Please try to guess the password: ")
  if guess == password:
    print("Access granted.")
    break #break is used to break out of a loop before the condition of the loop is met. Don't worry about this too much, but it is helpful to know about.
  else:
    print("Incorrect password. Try again.")
    attempts -= 1

#these conditionals are meant to be outside of the while loop, unlike the ones above

#first check if the amount of guesses is 0. If so, that means that the user never even got the password right. Print a message to the user.
if attempts == 0:
  print("You did not guess the password.")
#else, the user must have gotten the password right. Congratulate them.
else:
  print("CONGRATULATION!!!  You guessed the password!")
