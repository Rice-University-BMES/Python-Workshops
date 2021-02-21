# module 2 - Dictionaries

#author Eric Torres
#email edt3@rice.edu
#date 03 Feb 2021 

# dictionary is a mapping,
# keys -> values. one directional

import random

my_dict = {1:2, 3:4, 6:727, 83:421}
print(my_dict[3])

# cypher example!

CYPHER = {'a': 'x', 'b': 'c', 'c': 'r', 'd': 'm', 'e': 'l'}


def encode():
    emsg = ""
    for ch in message:
        emsg += CYPHER[ch]
    print(message, "encodes to", emsg)
    return (emsg)

def decode():
    dmsg = ""
    for ch in message:
        for key, value in CYPHER.items():
            if ch == value:
                dmsg += key
    print(message, "decodes to", dmsg)

message = 'abc'
encode()
message = 'xcr'
decode()

print("===")

new_cypher = "abcdefghijlkmnopqrstuvwxyz"
new_dict = {}

cyph_list = list(new_cypher)
random.shuffle(cyph_list)

for ch in new_cypher:
    new_dict[ch] = cyph_list.pop()

def new_encode():
    emsg = ""
    for ch in message:
        emsg += new_dict[ch]
    print(message, "encodes to", emsg)
    return (emsg)

def new_decode():
    dmsg = ""
    for ch in message:
        for key, value in new_dict.items():
            if ch == value:
                dmsg += key
    print(message, "decodes to", dmsg)

message = "bioeiscool"
message = new_encode()
new_decode()