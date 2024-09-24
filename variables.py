# Python is completely object oriented, and not "statically typed".
# You do not need to declare the variables before using them, or declare their type.
# Every variable in Python is an object.

# Numbers: Python supports two types of numbers: 
# 1) Integers (Whole Numbers)
# 2) Floating Point Numbers (Decimals)

# Integers:

myint = 12
print(myint)

# Floating Point Numbers (Decimals)

myfloat = 13.56
print(myfloat)
anotherfloat = float(56.13)
print(anotherfloat)

# Strings: Strings are defined either with a single quote or a double quotes.

mystring = 'namaste, duniya!'
print(mystring)
anotherstring = "hello, world!"
print(anotherstring)

# The difference between the two is the convenience of putting apostrophes.


# Simple Operators can be executed on numbers and strings:

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# Assignment Operators can be done on more than one variables "simultaneously" on the same line.

a, b, c = 10, 12, 15
print(a, b, c)

# Mixing Operators between numbers and strings is not supported:

# This program will not work

one = 1
two = 2
hello = "hello"

print (one + two + hello)

