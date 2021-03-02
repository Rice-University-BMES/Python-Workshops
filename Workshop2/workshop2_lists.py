# Python Workshop 2 - Lists

#author Eric Torres
#email edt3@rice.edu
#date 03 Feb 2021

# Create

# order matters in a list! order is preserved
# duplicate entries may exist in a list
numbers = [1, 3, 4, -7, 3, 43]
print(numbers)

groceries = ['milk', 'eggs', 'bread', 'butter']
print(groceries)

# ask how many elements are in this list
nested = [['b', 'i', 'o', 'e'], [2, 5, 2], []]
print(nested)

print("===")

print(len(groceries))
print(len(nested))

print("===")

# Access
print(groceries[0])
print(groceries[-1])
# print(nested[2])

essentials = groceries[2:4]
print(essentials)
ess2 = groceries[2:]
print(ess2)

print("===")

# Update

groceries[2] = 'cheese'
print(groceries)

nested[1] = [3, 2, 2]
print(nested)

# elements of lists can be changed, unlike strings
# brackets on right side of equals sign means access, brackets on left side means update
# note that good programming means homogenous lists! however, you can have different data types in a list

# List Methods

# like other python data types, there are built-in methods (aka functions) that can modify them!

classes = ['bioe 452', 'bioe 421']
print(classes)

classes.append('elec 327')
print(classes)

# in breakout rooms, can figure out what .reverse(), .insert() do
