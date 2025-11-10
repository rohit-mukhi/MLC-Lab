import numpy as np

arr = np.arange(20, 29).reshape(3, 3)
print("Original array: ")
print(arr)
print("The third row: ")
print(arr[2:])
print("The second column: ")
print(arr[:1])