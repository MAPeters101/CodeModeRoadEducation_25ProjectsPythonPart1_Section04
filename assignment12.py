shape = ""

while shape.lower() != "stop":
    shape = input(
        "\nWhat shape do you want to print? (triangle, square, pyramid) \n(Type STOP to end) ")

    if shape.lower() == "stop":
        break
    # create a while loop that keeps asking the user for a shape UNTIL they    enter "triange", "square", or "pyramid"

    height = int(input("\nHow tall do you want the shape to be? "))

    # while the height is less than or equal to zero, continue asking the user for a height

# For printing a right triangle:
# If the shape is "triangle":
#   Iterate through each row up to the height
#   In each row, print '*' for the number of times equal to the row number
#   This will create a right triangle

# For printing a square:
# If the shape is "square":
#   Iterate through each row up to the height
#   In each row, print '*' for the number of times equal to the height
#   This will create a square

# For printing a pyramid:
# If the shape is not "triangle" or "square":
#   Iterate through each row up to the height
#   In each row, print spaces for the number of times equal to (height - row number)
#   Then print '*' for the number of times equal to (2 * row number - 1)
#   This will create a pyramid with spaces and '*'s

