import numpy as np
from sklearn.neural_network import MLPRegressor


X = np.array([
    [2, 4, 1, 5, 6],
    [3, 1, 5, 6, 7],
    [1, 3, 6, 7, 8],
    [6, 6, 7, 8, 9]
])


autoencoder = MLPRegressor(
    hidden_layer_sizes=(3,),  
    activation='relu',
    max_iter=7000,
    random_state=42
)

autoencoder.fit(X, X)


W1 = autoencoder.coefs_[0]     
b1 = autoencoder.intercepts_[0]


compressed = np.maximum(0, np.dot(X, W1) + b1)  

print("Compressed 3D Representation:")
print(compressed)


reconstructed = autoencoder.predict(X)

print("\nReconstructed Output:")
print(reconstructed)

# See what error is this:
"""
/home/iter/.local/lib/python3.10/site-packages/sklearn/neural_network/_multilayer_perceptron.py:781: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (7000) reached and the optimization hasn't converged yet.
  warnings.warn(
"""
