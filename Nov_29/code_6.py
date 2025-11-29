from sklearn.linear_model import LassoCV
from sklearn.datasets import load_diabetes

diabetes = load_diabetes(as_frame=True)
df_d = diabetes.frame

x = df_d.iloc[:, :-1]
y = df_d.iloc[:, -1]

lasso = LassoCV(cv=5)
lasso.fit(x, y)

print("Coefficients", lasso.coef_)
print("Number of selected features: ", sum(lasso.coef_ != 0))
