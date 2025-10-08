import numpy as np

array_1d = np.arange(1, 31)

matrix_5x6 = array_1d.reshape(5, 6)

even_numbers = matrix_5x6[matrix_5x6 % 2 == 0]

average_of_evens = even_numbers.mean()

print(f"Average of the even numbers: {average_of_evens}")
