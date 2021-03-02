# Python Workshop 2 - iteration (for loops)

# author Eric Torres
# email edt3@rice.edu
# date 24 Feb 2021


# a good example is the check if odd example
numbers = [1, 7, 8, 42, 3, 4, 10, 12, 13, 15]

# python iterates through the elements in a list, as opposed to through indices!
# Does this for any iterable object (try it with a string or any iterable data type we cover!)
for num in numbers: # note the colon at the end of this line, and indentation of the following code
    print(num)

count = 0
for num in numbers: # note the colon at the end of this line, and indentation of the following code
    print("Iteration count = ", count, "Item = ", num)
    count += 1

# hi = "hello"
# for letter in hi:
#     print(letter)

# print(chr(69))
print("===")

# matlab version
for idx in range(len(numbers)):
    print(numbers[idx])

print(list(range(5)))
# range lets you choose start (inclusive), end (exclusive), and step size
print(list(range(5, 12)))
print(list(range(5, 12, 2)))

# similar to matlab's vec = [5:2:11];

print("===")


# print(len(numbers)) # len returns the length of an iterable object!
# num_range = range(len(numbers)) # range returns a list from starting value to ending value, exclusive
# print(num_range)
# print(list(num_range))

# should i talk about enumerate?
# print(list(enumerate(numbers)))



# editing a list - removing odd numbers


# edit list as you iterate over it, change elements that you have already checked!
def remove_odd(numbers):
    for num in numbers:
        if num % 2 == 1:
            numbers.remove(num)

print(numbers)
# remove_odd(numbers)
# print(numbers)

def remove_odd4(numbers):
    newnums = []
    for num in numbers:
        if num % 2 == 0:
            newnums.append(num)
    return newnums

print(remove_odd4(numbers))

# feel like this is not necessary
# def count_odd(numbers):
#     count = 0
#     for num in numbers:
#         if num % 2 == 1:
#             count += 1
#
#     return count
#
# # this might be useful actually for function stuff
# def check_odd(numbers):
#     odd = False
#     for num in numbers:
#         if num % 2 == 1:
#             odd = True
#     return odd
#
# # change check_odd, don't rewrite all of this
# def check_odd2(numbers):
#     for num in numbers:
#         if num % 2 == 1:
#             return True
#     return False
#
# def remove_odd2(numbers):
#     remove = []
#     for num in numbers:
#         if num % 2 == 1:
#             remove.append(numbers.index(num))
#
#     # walk through debugging!
#     for idx in remove:
#         numbers.pop(idx)
#     # what's happening? we're saving indices, but as we go to remove items, the list shifts items to the
#     # left to take in the spot of the removed item, so we will be indexing a spot that doesn't exist
#
# # copy + paste this one!
# def remove_odd3(numbers):
#     remove = []
#     for num in numbers:
#         if num % 2 == 1:
#             remove.append(num)
#
#     for num in remove:
#         numbers.remove(num)


# def run():
#     numbers = [1, 7, 8, 42, 3, 4, 10, 12, 13, 15]
#     print(numbers)
#     remove_odd3(numbers)
#     print(numbers)
#     print(remove_odd4(numbers))

# run()


# more for a conditionals/logic file
"""
hi = True
yo = False
print(hi | yo)
print(not hi)
print(not(hi or yo))
"""
# have at least one example showing elif, rixner's friend/money example is good