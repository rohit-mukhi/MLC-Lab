import pandas as pd
import numpy as np

arr1 = np.array([12, 24, 36, 48, 60, 72])
arr2 = np.array([17, 34, 51, 68, 85, 102])

x = pd.Series(arr1)
y = pd.Series(arr2)

# The head() function will print the first 5 elements
print(x.head())
print("")
print(y.head())

# To print the size of a series
# Look for this one...
print(x.Size())
