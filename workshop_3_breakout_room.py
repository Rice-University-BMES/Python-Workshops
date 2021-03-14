# Python Workshop 3 - breakout rooms

# author Sai Narendrula
# email sn42@rice.edu
# date March 14, 2021

# a file to help practice what we learned

# using list comprehension:
# import the numpy package and matplotlib.pyplot
# create an array from 0 to 50 with a step size of 6
# using numpy.arrange()

# using list comprehension, store all of the odd numbers in a new list



# dictionary comprehension
# (hint: use zip to bring the lists together, then access both items from each tuple!)

# Lists to represent keys and values
keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]



# plotting:

# using plt.scatter, plot the data from this file! (code below to read from the file) (note: using matplot.pyplot
# imported as plt)
data = np.genfromtxt('hw0_data.txt', delimiter='\t')  # note: this is using numpy imported as 'np'

x2 = [x[2] for x in data if x[2] != np.nan]
y2 = [x[3] for x in data if x[3] != np.nan]

x2.pop(0)
y2.pop(0)
