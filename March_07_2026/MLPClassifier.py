from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score

x, y = make_classification(n_samples=300, n_features=4, n_informative=4, n_redundant=0, random_state=1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

model = MLPClassifier(hidden_layer_sizes=(10, 5), activation='relu', learning_rate_init=0.1, max_iter=500, random_state=1)

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("Accuracy Score:", accuracy_score(y_test, y_pred))
