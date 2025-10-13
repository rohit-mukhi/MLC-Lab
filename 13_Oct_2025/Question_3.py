import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='red', marker='o', s=100, edgecolors='black', alpha=0.5, label='Scatter plot')
plt.legend(loc=9)
plt.show()
