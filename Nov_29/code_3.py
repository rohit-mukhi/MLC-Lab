from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.datasets import load_iris

iris = load_iris()
x, y = iris.data, iris.target

lda = LinearDiscriminantAnalysis(n_components=2)
x_lda = lda.fit_transform(x, y)

print("Original shape: ", x.shape)
print("Reduced shape: ", x_lda.shape)
