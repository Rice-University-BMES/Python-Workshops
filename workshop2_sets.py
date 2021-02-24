# Python Workshop 2 - lists

# author Eric Torres
# email edt3@rice.edu
# date 14 Feb 2021

# list - ordered sequence
# dictionary - key -> value mapping
# set - unordered collection of data with no duplicates

# like a list, but bc no order and no duplicates, faster to use than lists!
# list looks like [1, 2, 3, 2, 1]
# set looks like set([1, 2, 3]) - no duplicates!

### Sets

courses = set([252, 332, 370, 391]) # can also be written as {}
print(courses)

courses2 = set([252, 332, 252, 370, 391, 332])
print(courses2)

print(courses == courses2)

for course in courses:
    print(course)


courses.add(253)
print(courses)

courses.remove(332)
print(courses)

# can't remove items that are not currently in the set!
# courses.remove(369)
# print(courses)

# check if something is in a set
print(369 in courses)
print(332 in courses)
print(252 in courses)

# you can perform logical operations on sets to combine or remove items!
print(courses)
print(courses2)

courses3 = courses.union(courses2) # adds all items together into a set
print(courses3)
print(courses) # note that courses was not mutated!

courses3 = courses.intersection(courses2) # shows only items they have in common
print(courses3)

# courses3 = courses # what happens if i uncomment this line?

# what if you did want to update courses?
courses.intersection_update(courses2)
print(courses)