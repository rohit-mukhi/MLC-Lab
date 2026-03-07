import numpy as np

x = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])

np.random.seed(1)
weights = np.random.rand(2, 1)
learning_rate = 0.1

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

for epoch in range(5000):
    output = sigmoid(np.dot(x, weights))
    error = y - output
    adjustments = learning_rate * np.dot(x.T, error * sigmoid_derivative(output))
    weights += adjustments
    
print("Final output:")
print(output)
