#1
import numpy as np
array = np.array([i for i in range(1, 100)])
print(array)
#2
array = np.array([i for i in range(1, 100, 3)])
print(array)
#3
array = np.array([i for i in range(1, 100)])
print(array)
array_33 = np.array([array[3*i]+array[3*i+1]+array[3*i+2] for i in range (0,33)])
print(array_33)
#4
matrix = array_33.reshape(11, 3)
print(matrix)
#5
print(matrix.T)
#6
c = np.array([i for i in range(-9, 2)])
print(c)
print(matrix.T @ c)
#7
transp = matrix.T
print(transp)
print(transp[0::2, 0::4])
#8
matrix = array_33.reshape(11, 3)
print(matrix)
b = (matrix[2::3,:])
print(b)
print(np.linalg.det(b))

