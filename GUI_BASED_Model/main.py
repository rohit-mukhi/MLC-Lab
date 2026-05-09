import os
import joblib
import tkinter as tk
from tkinter import messagebox
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

def build_model():
    iris = load_iris()
    X = iris.data    
    y = iris.target 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=1)
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    joblib.dump(model, "iris_model.pkl")

def run_gui():
    if not os.path.exists("iris_model.pkl"):
        build_model()
        
    model = joblib.load("iris_model.pkl")
    iris = load_iris()

    root = tk.Tk()
    root.title("Iris Flower Classification")
    root.geometry("300x250")
    root.resizable(False, False)

    tk.Label(root, text="Iris Flower Prediction", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(root, text="Sepal Length:").grid(row=1, column=0, padx=10, pady=5)
    entry1 = tk.Entry(root)
    entry1.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Sepal Width:").grid(row=2, column=0, padx=10, pady=5)
    entry2 = tk.Entry(root)
    entry2.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(root, text="Petal Length:").grid(row=3, column=0, padx=10, pady=5)
    entry3 = tk.Entry(root)
    entry3.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(root, text="Petal Width:").grid(row=4, column=0, padx=10, pady=5)
    entry4 = tk.Entry(root)
    entry4.grid(row=4, column=1, padx=10, pady=5)

    def classify_flower():
        try:
            features = [[
                float(entry1.get()),
                float(entry2.get()),
                float(entry3.get()),
                float(entry4.get())
            ]]
            prediction = model.predict(features)
            flower_name = iris.target_names[prediction[0]]
            messagebox.showinfo("Prediction Result", f"The Iris flower is: {flower_name}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values.")

    predict_btn = tk.Button(root, text="Predict", command=classify_flower)
    predict_btn.grid(row=5, column=0, columnspan=2, pady=15)

    root.mainloop()

if __name__ == "__main__":
    run_gui()
