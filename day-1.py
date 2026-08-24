# My First Python Program 🎉

# Simple print statements to display text
print("Hello, world!")
print("It's a really good day today!")

# Variables

# A variable stores data that can change or be reused.
# Common data types include:
# - String (text)
# - Integer (whole number)
# - Float (decimal number)
# - Boolean (True/False)


# Strings

# f-strings (formatted strings) let you insert variables into a string using {}
# They're cleaner and easier to read than string concatenation

first_name = "Sayan"
last_name = 'Chakraborty'
food = "chhole bhature"
email = "sunny.dev@hotmail.com"

print(f"Heyy, I am {first_name} {last_name}")
print(f"I love {food}, and here's my email: {email}")

# Integers

age = 22
food_quantity = 4

print(f"Well, if you can't guess, I am {age} and I can absolutely murder {food_quantity} plates of {food} at a time.")

# Float

nyc_price = 10.99
ind_price = 30
distance = 100

print(f"damn it, I once saw the price of {food} at a restaurant in NYC for a whopping ${nyc_price}! Like what are they filling in it with GOLD?")
print(f"Thank god, Delhi has the tastiest stuff just for ₹{ind_price} and that too just {distance}m from my place.")

# Boolean
# Booleans represent true or false values. They are super useful for conditions.

is_available = False
gut_feeling = True

if gut_feeling:
    print("I think Manchester United won't be relegated")
else:
    print("Man United is doomed")

if is_available:
    print("I'll buy this year's man united shirt")
else:
    print("this year's shirts are absolute bollocks!")