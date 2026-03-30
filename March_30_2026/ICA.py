import numpy as np
from sklearn.decomposition import FastICA

S = np.array([
    [2/3, 1],
    [1, -2],
    [4, 1],
    [5, -2]
])

A = np.array([
    [2, 1],
    [1, 3]
])

X = np.dot(S, A)

print("Mixed Signals (X):")
print(X)


ica = FastICA(n_components=2, random_state=42)
S_recovered = ica.fit_transform(X)  
A_estimated = ica.mixing_           

print("\nRecovered Signals (S_hat):")
print(S_recovered)

print("\nEstimated Mixing Matrix:")
print(A_estimated)


print("\nOriginal Signals (S):")
print(S)
