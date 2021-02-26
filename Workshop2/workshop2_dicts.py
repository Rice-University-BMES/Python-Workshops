# Python Workshop 2 - dictionaries

# author Eric Torres
# email edt3@rice.edu
# date 03 Feb 2021

# dictionary is a mapping,
# keys -> values. one directional
# duplicate keys are NOT allowed!
import random

my_dict = {1:2, 3:4, 6:727, 83:421}
print(my_dict[3])
print(my_dict[83])
# print(my_dict[421])

# duplicates aren't allowed!
my_dict = {1:2, 3:4, 6:727, 83:421, 3:70, 6:49}
print(my_dict)

# dictionaries can map different data types, including lists! (like cabinets)
dict2 = {3: 'red', 5: 'blue', 6: 'red'}
print(dict2[5])

# cypher example!

CYPHER = {'a': 'x', 'b': 'c', 'c': 'r', 'd': 'm', 'e': 'l'}

# have these minimized already
def encode(message):
    emsg = ""
    for ch in message:
        emsg += CYPHER[ch]
    print(message, "encodes to", emsg)
    return emsg


def decode(message):
    dmsg = ""
    for ch in message:
        for key, value in CYPHER.items():
            if ch == value:
                dmsg += key
    print(message, "decodes to", dmsg)

encode('abc')
decode('xcr')

# could be useful for finding DNA complements, or the RNA version of it!

print("===")

# more advanced cypher!

# new_cypher = "abcdefghijlkmnopqrstuvwxyz"
# new_dict = {}
#
# cyph_list = list(new_cypher)
# random.shuffle(cyph_list)
#
# for ch in new_cypher:
#     new_dict[ch] = cyph_list.pop()
#
# def new_encode():
#     emsg = ""
#     for ch in message:
#         emsg += new_dict[ch]
#     print(message, "encodes to", emsg)
#     return (emsg)
#
# def new_decode():
#     dmsg = ""
#     for ch in message:
#         for key, value in new_dict.items():
#             if ch == value:
#                 dmsg += key
#     print(message, "decodes to", dmsg)
#
# message = "bioeiscool"
# message = new_encode()
# new_decode()