while True:
    try:
        num = int(input("Please enter an integer: "))
        break
    except ValueError:
        print("please enter an integer!")

print("Thank you for entering an integer.")