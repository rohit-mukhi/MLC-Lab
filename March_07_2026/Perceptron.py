import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score

x, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_clusters_per_class=1, random_state=123)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=123)

model = Perceptron(max_iter=1000, eta0=0.1)

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("Accuracy score:", accuracy_score(y_test, y_pred))
