import pandas as pd
import numpy as np

arr = np.array([14, 45, 67, 88])
x = pd.Series(arr , index=['A', 'B', 'C', 'D'])
# Adding index part is optional
print(x)

"""
Output:

0    14
1    45
2    67
3    88
dtype: int64\

"""
