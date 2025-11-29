from sklearn.feature_selection import SelectKBest, chi2

x_new = SelectKBest(chi2, k=2).fit_transform(iris.data, iris.target)

print("Original: ", iris.data.shape)
print("Reduced: ", x_new.shape)
