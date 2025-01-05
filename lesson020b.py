x = 0
num = int(input("Enter a number: "))

print(x)
if x < num:
    while x < num:
        x += 1
        print(x)
elif x > num:
    while x > num:
        x -= 1
        print(x)
