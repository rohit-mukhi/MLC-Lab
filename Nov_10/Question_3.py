import pandas as pd

data = pd.read_csv('stock.csv')
print("First 3 elements: ")
print(data.head(3))
print("\nLast 4 elements:")
print(data.tail())