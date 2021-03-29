# Rice BMES Python Workshop 4 - Classes/Object-Oriented Programming

# author Eric Torres
# email edt3@rice.edu
# date 27 Mar 2021

# Note summary of important points in this workshop!

"""

Classes/Object-Oriented Programming (OOP):

OOP combines data (like numbers, strings, etc.) with behaviors (like functions). It's useful for representing complex
concepts that we see in the real world!


Some definitions:

Class - a class is a general blueprint that describes what properties and behaviors objects of that class have
Object - an instance of a class (ex: actually making one case of that class, like when you define a variable)
Attribute - properties of the object (the data)
Methods - functions/behaviors that act on the data

Ex: person as a class
Class: Person
Object: Eric
- attributes: name, age
- methods: walking, breathing

the __init__ and __str__ methods are special methods in Python that are used to initialize and print(object), respectively.

the "self" argument must be included in method declarations, but is implicit when you call them

ex: in Character, I wrote get_health(self). When I want to get the health of a character object called Eric, I would type
Eric.get_health(). Essentially, python takes what's to the left of the period and inputs it in the self category, and this
lets python know that it's acting on the "Eric" object

note that methods defined in classes are only applicable to objects of that class, unlike regular python functions!

"""


class Character:

    def __init__(self, name, initial_health): # for most methods, you don't need to return anything unless you want to!
        self.name = name
        self.health = initial_health
        self.inventory = []

    # for __str__, the most important part is that it must return a string, which is what will be printed when you call
    # print(object_name)
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

# example1()

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
