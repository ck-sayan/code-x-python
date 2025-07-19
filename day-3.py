# input() = A function that prompts the user to enter data.
# The user input is registered as a string.

name = input("yo! what's your name?: ")
initial_age = float(input("well, how old are you buddy? You seem new to the dojo = "))

age = int(initial_age + 10)

print(f"welcome to the dojo, {name}! At {initial_age}, I was already a street fighting shark, you are late so let's start the training!")

print(f"for getting the black belt, you'll need to train until {age}")

# Practice Problems

## Calculate the area and perimeter of rectangle

length = float(input("Enter the length of the rectangle = "))
width = float(input("Enter the width of the rectangle = "))
per = 2*(length + width)
area = length*width

print(f"For a rectangle with length = {length} and breadth = {width}, the perimeter should be {per} and area should be {area}")


# Practice Problem:

## Calculate the area and perimeter of a square

side_square = float(input("Enter the length of side of the square = "))
per_square = 4*side_square
area_square = side_square*side_square

print(f"for a square of a side {side_square} and perimeter is {per_square} and area is {area_square}")