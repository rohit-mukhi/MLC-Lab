import numpy as np
from sklearn.decomposition import TruncatedSVD

x = np.random.rand(5, 4)

svd = TruncatedSVD(n_components=2)
x_svd = svd.fit_transform(x)

print("Original: ", x.shape)
print("Reduced: ", x_svd.shape)
