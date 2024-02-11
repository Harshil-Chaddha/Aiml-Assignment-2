#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

array_of_fives = np.full(10, 5)
print(array_of_fives)


# In[2]:


import numpy as np

array_of_integers = np.arange(10, 51)
print(array_of_integers)


# In[4]:


import numpy as np

# Create an array of even integers from 10 to 50
array_of_even_integers = np.arange(10, 51, 2)

print(array_of_even_integers)


# In[6]:


import numpy as np

# Create an array of values ranging from 0 to 8
array_values = np.arange(9)

# Reshape the array into a 3x3 matrix
matrix_3x3 = array_values.reshape(3, 3)

print(matrix_3x3)
#np.arange(9) creates an array with values from 0 to 8.
#reshape(3, 3) reshapes the 1D array into a 3x3 matrix.


# In[7]:


import numpy as np

# Generate an array of 25 random numbers sampled from a standard normal distribution
random_numbers = np.random.randn(25)

print(random_numbers)
#random.randn function to generate an array of random numbers


# In[8]:


import numpy as np

# Create an array from 0 to 1 with a step size of 0.01
result_array = np.arange(0, 1.01, 0.01)

print(result_array)
#arange function to generate an array of numbers ranging from 0 to 1 with a step size of 0.01


# In[9]:


import numpy as np

# Create an array of 20 linearly spaced points between 0 and 1
linear_points = np.linspace(0, 1, 20)

print(linear_points)
#linspace function to generate an array of linearly spaced points between 0 and 1


# In[10]:


import numpy as np

# Generate the matrix mat
mat = np.arange(1, 26).reshape(5, 5)

print("Matrix mat:")
print(mat)
print()

# Extract the specified submatrices using slicing/indexing
submatrix1 = mat[1:4, 1:]
submatrix2 = mat[1:4, :1]

print("Submatrix 1:")
print(submatrix1)
print()

print("Submatrix 2:")
print(submatrix2)
print()

# Get the sum of all values in mat
total_sum = np.sum(mat)
print("Sum of all values in mat:", total_sum)
print()

# Get the sum of all rows and columns in mat
row_sums = np.sum(mat, axis=1)
col_sums = np.sum(mat, axis=0)

print("Sum of each row in mat:", row_sums)
print("Sum of each column in mat:", col_sums)


# In[ ]:




