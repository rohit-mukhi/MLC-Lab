from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error

x, y = make_regression(n_samples=200, n_features=5, noise=10, random_state=0)

xtr, xte, ytr, yte, = train_test_split(x, y, test_size=0.3, random_state=0)

model = ElasticNet(alpha=0.1, l1_ratio=0.5)

model.fit(xtr, ytr)

y_pred = model.predict(xte)

print("Mean Squared Error: ", mean_squared_error(yte, y_pred))
