import numpy as np

X = np.array([1, 2, 3, 5, 6]).reshape(-1, 1)
y = np.array([0, 0, 1, 1, 1])

centers = np.array([2, 5])
sigma = 1.5

def rbf(x, c, sigma):
    return np.exp(-((x - c) ** 2) / (2 * sigma ** 2))

H = np.zeros((len(X), len(centers)))

for i in range(len(X)):
    for j in range(len(centers)):
        H[i, j] = rbf(X[i], centers[j], sigma)

W = np.linalg.pinv(H) @ y

y_pred = H @ W
y_class = (y_pred >= 0.5).astype(int)

print("Hidden Layer Matrix:\n", H)
print("\nWeights:\n", W)
print("\nPredictions:\n", y_class)
