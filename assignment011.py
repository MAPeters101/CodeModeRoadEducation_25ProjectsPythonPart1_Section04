print("Even-Odd Number Checker\n")

choice = ""
while choice != "STOP":
    while True:
        # inside of a try block, ask the user for a number, and break from the block after.
        try:
            number = int(input("Please enter an integer: "))
            break
        # inside of the except block, check for a value error. If there is a value error, the code inside of this block will run. The only code that needs to run is a message stating that the user must enter a number.
        except ValueError:
            print("Please enter an integer!")

    # now outside of the while true loop, you need to check if the user's number is even or odd. Remember, you must use the modulo (%) operator to check if the user's number divided by 2 has a remainder of 0. If it does, the number is even. Else, the number is not
    if number%2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
    choice = input("Do you still want to play? (Enter STOP to stop playing): ")

