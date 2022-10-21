import numpy as np
np.random.seed(42)
array = np.random.randint(50, size=49)
matrix = array.reshape(7, 7)
print(matrix)
matrix = np.delete(matrix,(5), axis=0)
matrix = np.delete(matrix,(5), axis=1)
print(matrix)
print(np.linalg.det(matrix))