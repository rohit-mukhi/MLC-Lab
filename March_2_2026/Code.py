import numpy as np

class Perceptron:
    def __init__(self, lr=0.1, epochs=10):
        self.lr = lr
        self.epochs = epochs

    def activation(self, x):
        return 1 if x >= 0 else -1

    def fit(self, x, y):
        self.weights = np.zeros(x.shape[1])
        self.bias = 0

        for _ in range(self.epochs):
            for i in range(len(x)):
                linear = np.dot(x[i], self.weights) + self.bias
                y_pred = self.activation(linear)

                update = self.lr * (y[i] - y_pred)
                self.weights += update * x[i]
                self.bias += update

    def predict(self, x):
        linear = np.dot(x, self.weights) + self.bias
        return self.activation(linear)


# Sample data
x = np.array([[2,3], [1,1], [2,1], [-1,-2]])
y = np.array([1, 1, -1, -1])

p = Perceptron(lr=0.1, epochs=10)
p.fit(x, y)

print("Prediction:", p.predict(np.array([2,2])))
