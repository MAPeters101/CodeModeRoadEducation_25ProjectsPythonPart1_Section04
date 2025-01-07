string = "I love Python!"
count = 0

char_value = input("Please enter a character to count: ")

for char in string:
    if char.lower() == char_value.lower():
        count += 1

print(f"'{char_value}' appears in \"{string}\" {count} times.")


