# Breakout room activities for workshop 2!
# For/while loops, if statements, lists, sets, tuples, dictionaries

# TODO: add one more example with dictionaries!

# Lists

# It's time to make your schedule on python! make a list with all the classes you are currently taking
class_list = [] # enter your classes here!

# Now you have to plan for next semester! Add one class you will be taking next semester (using a list method from the
# CodeSkulptor Docs)


# Congrats, you're now able to drop the hardest class you have (if it's not a BIOE class, of course). Remove a class
# from your list (hint: try pop or remove, and understand how they're different!)


# Here's a list of all the numbers from 0 to 50, exclusive (aka doesn't include 50)
# Now, write a function that prints out all of the odd numbers! (hint, use the '%' operator)
numlist = list(range(50))


# Sets

# add, clear, copy, difference, discard, intersection (update), pop, remove, union (update)

# We have a set with the numbers 0 and 5, but now we want to add numbers from a list into this set!
# Write code to add the elements of the list into our given set
st = {0, 5} # can also do set([0, 5])
lst = [1, 2, 3, 4, 2, 2]


# Now that we have our set, we want to see if it matches our set of reference data
# Write code to show the values these two sets have in common! (hint: check the CodeSkulptor Docs for helpful methods)
st2 = {3, 5, 6, 7, 8}


# Dictionaries

# We made a dictionary with common fruits and what color they are!
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'raspberry': 'red', 'orange': 'orange', 'blueberry': 'blue'}

# From the following dictionary, print out all the fruits that are the color red (
for fruits in fruit_colors.keys():
    if fruit_colors[fruits] == 'red':
        print(fruits)

for fruits, colors in fruit_colors.items():
    if colors == 'red':
        print(fruits)


# Turns out the apple was supposed to be a Granny Smith. Can you change the 'apple' entry appropriately?

# ideas: swap keys and values
# nested dictionaries or lists

# other idea: make a function that adds numbers to a dictionary. key is number, value is number^2
dictiii = {1: 1, 2: 4, 3: 9, 4: 16}