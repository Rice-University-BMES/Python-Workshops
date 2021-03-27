# Rice BMES Python Workshop 4 - 

# author Eric Torres
# email edt3@rice.edu
# date 27 Mar 2021


class Character:

    def __init__(self, name, initial_health):
        self.name = name
        self.health = initial_health
        self.inventory = []

    def __str__(self):
        s = "Name: " + self.name
        s += " Health: " + str(self.health)
        s += " Inventory: " + str(self.inventory)
        return s

    def grab(self, item):
        self.inventory.append(item)

    def get_health(self):
        return self.health


eric = Character("Eric", 100)
print(eric)
eric.grab("pencil")
eric.grab("paper")
print(eric)
print(eric.get_health())

# an example to look at on your own!
class Dog:
    
    species = "Caninis familiaris"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        # can show as like s = self.name + "is " + str(self.age) + " years old". then return s
        return f'{self.name} is {self.age} years old'  # several ways to format strings. putting f before indicates format, and {} indicates a variable will be inside

    # same as doing the __str__ method!
    def description(self):
        return "{} is {} years old".format(self.name, self.age) # another string format method: self.name and self.age are substituted where the {} are

    def speak(self, sound):
        print(self.name + " says " + sound)

    def bark(self):
        print("woof!")
    
def example1():

    yorkie = Dog("chowder", 3)
    print(yorkie)
    yorkie.speak("hello")
    yorkie.bark()


    # you can delete classes, objects, or attributes of specific objects you instantiate!
    # you can also delete variables (including items in lists/dicts)

    del yorkie.name
    # print(yorkie)  # returns an error!
    yorkie.name = "rex"
    yorkie.fur_color = "brown"
    print(yorkie.name + " has " + yorkie.fur_color + " fur")

    poodle = Dog("bowser", 4)
    # print(poodle.fur_color)  # returns an error!

example1()

# another example to look at    
class Rectangle:
    """
    Geometric rectangle - initialize with width and height of the rectangle
    
    methods perimeter and area calculate the perimeter and area of the rectangle, respectively

    """
    
    def __init__(self, width, height):
        self._width = width
        self._height = height
        
    def perimeter(self):
        return 2 * self._width + 2 * self.height
    
    def area(self):
        return self._width * self._height


###################################################################################################

"""

Recursion: it's a way to make complex programs more succinct

it involves writing a function that calls itself from within, but with less data (otherwise it would run forever)

it works best when the data is composed of common sub-structures


define a base case and a recursive case
- base: when you know the answer to it, can solve directly (without calling the function again)
- recursive: when you don't and can break down the problem a small step

"""

# Recursion
def sum_up_to(n):
    if n == 1:
        # Base case
        return 1
    else:
        # Recursive case
        return n + sum_up_to(n-1)
    
print(sum_up_to(3))
print(sum_up_to(15))


# Same thing as...
print(sum(range(16))) # Just showing how recursion works, not necessarily convenient


def is_palindrome(word):
    if len(word) < 2:
        # Base case
        return True
    else:
        # Recursive case
        if word[0] != word[-1]:
            return False
        else:
            return is_palindrome(word[1:-1])
        
# if word is at 0 or 1 letters, you are at the center of the word, and it is then a palindrome
print(is_palindrome("aa"))
print(is_palindrome("BIOE"))
print(is_palindrome("BIOEOIB"))


print("===")

# another example you can look at on your own!
class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')
