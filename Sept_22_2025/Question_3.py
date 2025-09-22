import pandas as pd
import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([35, 34, 33, 32])

x1 = pd.Series(arr1)
x2 = pd.Series(arr2)

my_sum = pd.Series(x1 + x2)

print(my_sum)
