# Python Workshop 3 - numpy and matplotlib

# author Sai Narendrula
# email sn42@rice.edu
# date April 3, 2021

# The main objective of numpy module is to handle or create single- or multi- dimensional arrays.
# It is one of the backend engines for Pandas and other modules such as
# sklearn, scipy, etc., to handle array manipulation.

# To use packages, you need to import them
# Make sure they are available in your environment

import numpy as np

# to create an array, you use create from a list

array_example = np.array([1, 2, 3, 4, 5])

print(array_example)
print(array_example[0])
print('***********************')

# Using list of lists, we can create a 2D array
array2_ = np.array([[1, 2, 3], [4, 5, 6]])
print(array2_)
print('***********************')

# Multi dimension array
array3_ = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[1, 8, 5], [4,
2, 9]]])
print(array3_)
print('***********************')
# use .shape to see
print(array3_.shape)


# to create an array with placeholders
array_pc_1 = np.zeros(5)
array_pc_2 = np.ones(5)
print(array_pc_1)
print('***********************')
print(array_pc_2)


# linspace - array of equally spaced elements

array_eq = np.linspace(start=0, stop=10, num=10)
print(array_eq)
# arrange - array of equally spaced elements with given stepsize

array_eq_ss = np.arange(start=0, stop=10, step=1)
print(array_eq_ss)


# Matrix multiplication

a = np.array([11, 5, 7, 12, 2, 3, 15, 7, 9, 3, 5, 9])
b = np.array([4, 5, 8, 12, 3, 3, 12, 8, 9, 5, 6, 8])

C = a@b
print(C)


# Matplotlib is a low level graph plotting library in python that serves as a visualization utility

import matplotlib.pyplot as plt

plt.scatter(a, b)
plt.show()

plt.plot(array_eq, array_eq_ss)
plt.show()

