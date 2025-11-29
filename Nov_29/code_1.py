from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

iris = load_iris()
x = iris.data

pca = PCA(n_components=2)
x_pca = pca.fit_transform(x)

print("Original shape: ", x.shape)
print("Reduced shape: ", x_pca.shape)
