import numpy as np

class Adaline:
    def __init__(self, lr=0.01, epochs=20):
        self.lr = lr
        self.epochs = epochs

    def fit(self, x, y):
        self.weights = np.zeros(x.shape[1])
        self.bias = 0

        for _ in range(self.epochs):
            for i in range(len(x)):
                y_sum = np.dot(x[i], self.weights) + self.bias
                error = y[i] - y_sum

                # LMS (Delta rule) update
                self.weights += self.lr * error * x[i]
                self.bias += self.lr * error

    def predict(self, x):
        y_sum = np.dot(x, self.weights) + self.bias
        return 1 if y_sum >= 0 else -1


# Sample data
x = np.array([[1,2], [2,3], [3,4], [-1,-2]])
y = np.array([1, 1, 1, -1])

a = Adaline(lr=0.01, epochs=20)
a.fit(x, y)

print("Prediction:", a.predict(np.array([2,2])))
