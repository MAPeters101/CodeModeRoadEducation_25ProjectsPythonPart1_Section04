product = 1

while True:
    num = int(input("Enter an integer (-1 to stop): "))
    if num == -1:
        break
    product *= num

print(f"The product of all numbers is {product}.")