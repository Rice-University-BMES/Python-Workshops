# Python Workshop 1 - variables, data types, arithmetic operations, functions

# author Carrigan Hudgins
# email cdh5@rice.edu
# date 14 Feb 2021


# Comments! Be sure to comment your code for your future reference and for others to understand
# To block comment/uncomment, the keyboard shortcut is command + /

print("==========")

# Variables
# Variable names can contain letters, numbers, and underscores. Best practice is to separate words in your
# variable names with underscores.
this_year = 2021
last_year = 2020
print(this_year, last_year)
print("current year:", this_year)

# To refactor variables: right click variable name -> refactor -> rename

# References to immutable numbers. Note that when the last_year variable is changed to 2021, worst_year
# will still reference 2020.
worst_year = last_year
print(worst_year)
last_year = 2021
print(worst_year, last_year)

print("==========")

# Data types: integers and floats
print(1)
print(1.1)
print(int(1.1))
print(int(1.7))  # Note that the int command truncates
print(float(1))

# Data types: strings
s1 = 'Python is fun'
s2 = 'Yay BIOE'
print(s1)
print(s2)

s3 = '''Use triple quotes
for multiple lines!'''
print(s3)

print("==========")

# Basic arithmetic operations
print(2 + 2)  # addition
print(10 - 3)  # subtraction
print(5 * 4)  # multiplication
print(5 / 2)  # division
print(5 // 2)  # integer division
print(2 ** 3)  # exponentiation

# Modular arithmetic: returns the remainder of the divison
print(10 % 3)  # 10 mod 3 will print remainder 1
print(10 % 2)

print(((3 + 2) / (6 - 3)) / 4)  # when combining multiple operations, use parentheses. Don't rely on PEMDAS.

print("==========")

# Functions
def rectangle_area(side1, side2):
    """
    Compute the area of a rectangle.

    :param side1: float representing length of one side
    :param side2: float representing length of side adjacent to side1
    :return: area of rectangle with given side lengths
    """
    area = side1 * side2
    return area


# Note that you can designate the output of a function to a variable or print the output directly
area1 = rectangle_area(4, 5)
print(area1)
print(rectangle_area(4, 5))


# Functions without returns will return None. Functions don't always need inputs.
def hello():
    """
    Prints Hello World
    :return: None
    """
    print("Hello World")


hello()
result = hello()
print(result)
