import pandas as pd
import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([35, 34, 33, 32])

arr3 = np.array([15, 15, 15])

x1 = pd.Series(arr1)
x2 = pd.Series(arr2)
x3 = pd.Series(arr3)

# Simply adding cardinally alike series will retain their datatype
my_sum = pd.Series(x1 + x2)

# when adding less elements, the outputs are stored as floats
new_sum = pd.Series(x1 + x2 + x3)

print(my_sum)
print("")
print(new_sum)
