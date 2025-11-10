import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('sales.csv')

x = data['month']
y = data['profit']

plt.plot(x, y)

plt.xlabel("Month")
plt.ylabel("Profit")
plt.title("Monthly profit chart")
plt.grid(True)
plt.yticks(y)
plt.show()
