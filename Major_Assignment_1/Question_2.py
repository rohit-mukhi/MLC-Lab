import numpy as np

arr = np.arange(1, 17).reshape(4, 4)
print("Original matrix:")
print(arr)
print("")
extracted_arr = arr[2:4, 0:2]
print("extracted_arr: ")
print(extracted_arr)

determinant = np.linalg.det(extracted_arr)
print(f"The determinant of left bottom sub-matrix is: {determinant}")
