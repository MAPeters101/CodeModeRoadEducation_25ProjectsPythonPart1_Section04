num = 0
sum = 0

while num != -1:
    num = int(input("Enter a positive integer (or -1 to stop): "))
    if num == -1:
        break
    sum += num

print(f"The sum is: {sum}")