import numpy as np

# reshape is used to create an array of nxm dimensions
arr = np.arange(1, 13).reshape(3, 4)

print(arr)
print("")

# ravel is used to convert nxm dimension array to 1D
arr = np.ravel(arr)

print(arr)
