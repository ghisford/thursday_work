# Numpy Array Quiz
# Question 1
# What is the result of the following code?

#     import numpy as np
#     a = np.array([1, 2, 3])
#     b = np.array([4, 5, 6])
#     c = a + b
#     print(c)

[5,7,9]



# Question 2
# Create a numpy array of 10 zeros. and reshape it to (2, 5)

arr = np.array([0,0,0,0,0,0,0,0,0,0])
arr = arr.reshape(2,5)
print(arr)

# Question 3
# Find Mean, Mode, Median, Standard Deviation of the following data

import numpy as np
import statistics as st

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
arr = np.array(data)
mean = arr.mean()
mode = st.mode(arr)
median = np.median(arr)
std_dev = st.stdev(arr)

# Question 4
# create a 6x6 numpy array with random values and find the min and max values


arr = np.array([[1,2,4,6,7,8,],[0,9,8,7,6,5]])
min = arr.flatten().min()
max = arr.flatten().max()


# Question 5
# create a 3D numpy array and reshape it to 2D

import numpy as np
arr  = np.array([[[1,2],[3,4],[4,5]],[[7,8],[9,10],[11,12]]])
arr = arr.reshape(2,6)
arr
# Question 6
# create 1D array from this data

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr = np.array(data)
arr = arr.reshape(9,)

