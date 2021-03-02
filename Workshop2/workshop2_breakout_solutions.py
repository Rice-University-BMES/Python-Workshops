# Python Workshop 2 - breakout rooms: lists, dictionaries, sets, tuples, iteration, indexing

# author Eric Torres, Carrigan Hudgins, Saideep Narendula
# email edt3@rice.edu, cdh5@rice.edu, sn42@rice.edu
# date 28 Feb 2021

# Breakout room activities for workshop 2!
# For/while loops, if statements, lists, sets, tuples, dictionaries

# Lists

# It's time to make your schedule on python! make a list with all the classes you are currently taking
class_list = [252, 202, 211]  # enter your classes here!

# Now you have to plan for next semester! Add one class you will be taking next semester (using a list method from the
# CodeSkulptor Docs)
class_list.append(243)
print(class_list)

# Congrats, you're now able to drop the hardest class you have (if it's not a BIOE class, of course). Remove a class
# from your list (hint: try pop or remove, and understand how they're different!)
class_list.remove(252)
print(class_list)
class_list.pop(1)
print(class_list)

# Here's a list of all the numbers from 0 to 50, exclusive (aka doesn't include 50)
# Now, write a function that prints out all of the odd numbers! (hint, use the '%' operator)
numlist = list(range(50))
for num in numlist:
    if num % 2 == 1:
        print(num)

print("===========")

# Sets

# We have a set with the numbers 0 and 5, but now we want to add numbers from a list into this set!
# Write code to add the elements of the list into our given set
st = {0, 5}
lst = [1, 2, 3, 4, 2, 2]

combined_set = st.union(set(lst))
print(combined_set)

# Write code to show the values these two sets have in common! (hint: check the CodeSkulptor Docs for helpful methods)
st2 = {3, 5, 6, 7, 8}
common_set = st2.intersection(combined_set)
print(common_set)

print("==========")

# Dictionaries

# We made a dictionary with common fruits and what color they are!
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'raspberry': 'red', 'orange': 'orange', 'blueberry': 'blue'}

# From the above dictionary, write code to print out all the fruits that are the color red

for fruit, color in fruit_colors.items():
    if color == 'red':
        print(fruit)

# Turns out the apple was supposed to be a Granny Smith. Can you change the 'apple' entry appropriately?
fruit_colors['apple'] = 'green'
print(fruit_colors)

# We went through the BIOE core course requirements and were able to get this data off of the website
# However, we were only able to compile all the department names and course numbers, in order. Can you
# convert this to a dictionary that links the course number (key) to the department (value)?

course_nums = [252, 140, 202, 243, 211, 451]
depts = ['BIOE', 'COMP', 'MECH', 'ELEC', 'CHEM', 'BIOE']

course_dict = {}
for i in range(len(course_nums)):
    course_dict[course_nums[i]] = depts[i]

print(course_dict)

# You can also do this with the zip method shown below! Check out zip and enumerate in the
# Codeskulptor documentation.

zip_list = zip(course_nums, depts)
dict2 = {}
for course_num, dept in zip_list:
    dict2[course_num] = dept

print(dict2)