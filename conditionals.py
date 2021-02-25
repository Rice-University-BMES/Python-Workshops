# Python Workshop X - conditionals (if/elif/else, boolean logic)

# logic and conditionals

# logic operators


"""
>
<
>=
<=
==
&
|

# changes from matlab
!= (same as "not")
and (&& does NOT work)
or (|| does NOT work)
not (same as !=)
True (capitalized)
False (capitalized)
in (like "any" in matlab)
"""


# conditionals

print(True or False)
print(not True or False)
print(not(True or False))

print(2 > 5)
print("hello" == "hello")

print("===")

lst = [1, 2, 3]
print(1 in lst)
print(4 in lst)

print("===")

# this whole example below might just not be worth it


def greet(friend, money):
    if friend and money > 20:  # first change (just friend)
        print("Hi!")  # original
        money -= 20  # original
    elif friend:  # third change
        print("Hello")
    else:  # second change (make it print hello) # third change, print howdy and add 10 money
        print("Howdy, this is a stickup")
        money += 10
    return money


money = 15

money = greet(True, money)
print("Money:", money)

money = greet(False, money)
print("Money:", money)

money = greet(True, money)
print("Money:", money)

# object equivalence

lst = [1, 2, 3]
# lst2 = [1, 2, 3]  # change to lst2 = lst
lst2 = lst
print(lst is lst2)
print(lst == lst2)

# do this after changing lst2 = lst
lst2[2] = 4
print(lst)
print(lst2)

# now try with strings!
msg = "hello"
msg2 = msg
msg2[4] = "z"
print(msg)

# what would happen if this was a tuple? depends on whether or not we have covered tuples yet haha
