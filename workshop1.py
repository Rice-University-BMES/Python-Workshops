# Comments! Use comments to explain your code.


# Variables: reusable names
# Can contain letters, numbers, underscores
# Best practice: separate words with underscores, use meaningful names
# TODO: Fix Bug

current_year = 2021
last_year = 2020
print(current_year)
print(last_year)
print(current_year, last_year)
print('current year:', current_year)

# Show how to refactor variables

# Variable naming
worst_year = last_year
print(worst_year)
last_year = 2021
print(last_year, worst_year)

# show how to block comment/uncomment (command /)

# Data types

# integer
print(1)
# float
print(1.1)

# int to convert float to integer, truncates
print(int(1.1))
print(int(1.7))

# float to convert integer
print(float(1))

# string
s1 = 'Python is fun'
s2 = "yay Python"  # note that you can use double or single quotes

print(s1)
print(s2)

s3 = '''Use triple quotes
for multiple
lines!'''

print(s3)

# Arithmetic operations
print(2 + 2)
print(10 - 3)
print(5 * 4)
print(5 / 2)
# integer division
print(5 // 2)
print(2 ** 3)

# Best practice: use parentheses, don't rely on pemdas
print(3 + 2 / 6 - 3 / 4)


# mod arithmetic: useful for finding out if number is even or odd or finding the remainder


# Functions: remember order of operations and indentation/spacing

# should always include docstrings in the functions you write...basically provide documentation for your functions
def rectangle_area(side_1, side_2):
    """
    Write statement of what function does: Compute the area of a rectangle

    :param side_1: float representing length of one side
    :param side_2: float representing length of side adjacent to side_1
    (include the data type when describing your inputs)

    :return: area of rectangle with given side lengths
    """
    area = side_1 * side_2
    return area


# if you're used to matlab, you know that you write functions and include the outputs and inputs in your function
# definition. in python, the outputs are in the return statement at the end.

# to call the function:
area1 = rectangle_area(4, 5)
print(area1)
# notice that printing area won't work. This is just the variable name of the value the function returns. We need to
# designate a name to accept the output, which was area 1.
print(area)


# can also create functions with no return statements but that have print statements
def hello():
    """
    Prints Hello World

    :return: None
    """
    print("Hello World!")


hello()
result = hello()
print(result)