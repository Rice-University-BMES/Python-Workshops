# Python Workshop 2 - tuples

# author Eric Torres
# email edt3@rice.edu
# date 03 Feb 2021

# tuples are like lists but they are not mutable (aka changeable)!

lst = [1, 2, 3]
tup = (1, 2, 3)

print(lst)
print(tup)

print(type(lst))
print(type(tup))

print('===')

a = [4, 5, 6]
a[1] = 100
print(a)

# b = (4, 5, 6)
# b[1] = 100
# print(b)

print('===')

# why tuples? can be useful in projects where multiple people may be accessing data, to prevent
# any accidental changes

# how could you edit a tuple? you can convert to a list, edit, and convert back to a tuple!

old_tuple = (5, 10, 3, 2)

l = list(old_tuple)
l.reverse()

new_tuple = tuple(l)

print(old_tuple)
print(new_tuple)

# what if you want to make a copy of a tuple?

new_tuple = tuple(old_tuple)
print(old_tuple, new_tuple)
print(old_tuple is not new_tuple) # note that this is the same object!

new_tuple = list(tuple(old_tuple))
print(old_tuple is not new_tuple)


# how to copy a list
old_list = [1, 2, 3]
new_list = list(old_list)
print(old_list is not new_list)