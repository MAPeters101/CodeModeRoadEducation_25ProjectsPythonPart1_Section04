secretWord = "Python"

maxAttempts = 3

while maxAttempts > 0:
    guess = input("Guess a letter that's in the secret word: ")
    if guess in secretWord.lower():
        print(f"Correct!! {guess} is in {secretWord}.")
        break
    else:
        print(f"Sorry, {guess} is not in the secret word.")

    maxAttempts -= 1

if maxAttempts == 0:
    print(f"You ran out of attempts, the word was {secretWord}.")

