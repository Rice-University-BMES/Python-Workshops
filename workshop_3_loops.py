# Python Workshop 3 - loops

# author Sai Narendrula
# email sn42@rice.edu
# date April 3, 2021

# for and while loops allow us to iterate over data structures

# for item in data:
#   ** code **


class_list = ['452', '372', '203']
for num in class_list:
    print(num)  # prints the item stored in num for the iteration

print('***********************')
# can iterate through strings
for char in 'banana':
    print(char)

print('***********************')
# break condition
for num in class_list:
    print(num)
    if num == '372':
        break

# list comprehension
# newlist = [expression for item in iterable if condition == True]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

# long method
for x in fruits:
    if "a" in x:
        newlist.append(x)

# short method
newlist_short = [x for x in fruits if "a" in x]

print(newlist)
print(newlist_short)
print('***********************')
print([x ** 2 for x in range(5)])
print('***********************')

# while (condition):
#   ** code **

# normal while loop
i = 0
while i < 6:
    print(i)
    i += 1

print('***********************')
# break condition
j = 0
while j < 6:
    print(j)
    if j > 3:
        break
    j += 1

print('***********************')
# continue - stops current iteration and goes to next
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

print('***********************')
# while with an else statement - useful for having an end statement
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

print('***********************')

# nested dictionaries
# they can be used to store different information

teachers = {1: {'name': 'Carrigan', 'age': '21', 'major': 'BIOE'},
            2: {'name': 'Eric', 'age': '21', 'major': 'BIOE'}}

print(teachers[1]['age'])
print('***********************')
# to add more to a nested list, you need to call the new key with an empty dictionary
teachers[3] = {}

teachers[3]['name'] = 'Sai'
teachers[3]['age'] = '21'
teachers[3]['major'] = 'BIOE maybe?'

print(teachers[3])

print('***********************')
for t_id, t_info in teachers.items():
    print("\nTeacher ID:", t_id)

    for key in t_info:
        print(key + ':', t_info[key])

# can use "del" to delete values or whole dictionaries based on an index
del teachers[1]['name']
# pop can be used in a similar manner
# to remove specific values, use .remove
