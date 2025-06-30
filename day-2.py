# Typecasting = The process of converting a variable from one data type to another. 
# str(), int(), float(), bool()

name = "Sayan Chakraborty"
age = 22
gpa = 3.2
is_student = False

# Identify the data type of a value or a variable using = type(variable). ex: type(name) returns <class 'str'>

print(type(is_student))

# Typecasting

is_student = float(is_student)
print(is_student)