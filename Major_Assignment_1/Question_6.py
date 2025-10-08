import numpy as np

arr = np.array([1, 4, 2, 5, 7, 8, 9, 3, 6]).reshape(3, 3)
print("The original matrix is: ")
print(arr, "\n")

print("The transpose of the matrix is: \n")
print(np.linalg.matrix_transpose(arr), "\n")

print("The inverse of the matrix is: \n")
print(np.linalg.inv(arr))
