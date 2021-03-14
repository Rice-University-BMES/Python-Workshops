# Python Workshop 3 - breakout rooms

# author Sai Narendrula
# email sn42@rice.edu
# date April 3, 2021

# a file to help practice what we learned

# using list comprehension

# import the numpy package and matplotlib.pyplot

# create an array from 0 to 50 with a step size of 6
# using numpy.arrange()

# using list comprehension, store all of the odd numbers in a new list

# using plt.scatter, plot the data from this file!
data = np.genfromtxt('hw0_data.txt', delimiter='\t')

x2 = [x[2] for x in data if x[2] != np.nan]  # note: this is using numpy imported as 'np'
y2 = [x[3] for x in data if x[3] != np.nan]

x2.pop(0)
y2.pop(0)
