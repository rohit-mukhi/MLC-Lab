 # This program is used to do matrix multiplication, determinant and inverse of two matrices

import numpy as np

arr1 = np.arange(1, 10).reshape(3, 3)
arr2 = np.arange(11, 20).reshape(3, 3)
pro = np.full((3, 3), 0)

print("Result of matrix multiplication is : ")
# This is matrix multiplication
pro = arr1 * arr2
print(pro)
print("")
# This is determinant

det1 = np.linalg.det(arr1)
det2 = np.linalg.det(arr2)

print(f"Determinant of 1st matrix: {det1}")
print(f"Determinant of 2nd matrix : {det2}")

print("")

print("Inverse of 1st matrix: ")
inv1 = np.linalg.inv(arr1)
print(inv1)

print("")

print("Inverse of second matrix: ")
inv2 = np.linalg.inv(arr2)
print(inv2)
