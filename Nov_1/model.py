import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('auto_mpg(1).csv')

x = df.drop('class', axis=1) 
y = df['class']


le = LabelEncoder()

y_encoded = le.fit_transform(y) 


x_train, x_test, y_train, y_test = train_test_split(x, y_encoded, test_size=0.3, random_state=100)


lr = LinearRegression()

lr.fit(x_train, y_train) 

y_lr_train_pred = lr.predict(x_train)
y_lr_test_pred = lr.predict(x_test)


y_lr_mse = mean_squared_error(y_test, y_lr_test_pred)
y_lr_r2 = r2_score(y_test, y_lr_test_pred)


y_lr_cfm = confusion_matrix(y_test, y_lr_test_pred.round().astype(int)) 

print(f"Mean Squared Error: {y_lr_mse:.4f}\n")
print(f"R2 Score: {y_lr_r2:.4f}\n")
print("Confusion Matrix:\n", y_lr_cfm, "\n")
