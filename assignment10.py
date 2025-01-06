print("Welcome to the Wall of Zeros And Ones\n")
#create a for loop that loops 10 times (make sure the iteration variable is called i for the purposes of this project)
for i in range(10):
    #INSIDE of the for loop loop, create another for loop that loops 10 times (make sure the iteration variable is NOT called i) ALSO, make sure to copy and paste the two conditionals below to be INSIDE of THIS FOR LOOP
    for j in range(10):
        if i % 2 == 0:
          print('0', end='') #determine what needs to be printed if the current iteration is even (the row is odd)
        if i % 2 != 0:
          print('1', end='') #determine what needs to be printed if the current iteration is odd (the row is even)

    #type the line of code that we use to skip to the next row
    print()
