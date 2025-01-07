word = input("Enter a random word: ")
letter = input("Enter a random letter: ")

word = word.lower()
letter = letter.lower()

count = 0

for char in word:
    if char == letter:
        count += 1

print(f"The letter {letter} appears in the word {word} {count} times.")
