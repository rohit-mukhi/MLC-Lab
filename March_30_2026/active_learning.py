import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

X, y = make_classification(
    n_samples=150,
    n_informative=2,
    n_redundant=0,
    n_repeated=0,
    n_features=3,
    n_classes=2,
    random_state=42
)

labeled_idx = list(range(15))             
unlabeled_idx = list(range(15, 150))       

X_labeled = X[labeled_idx]
y_labeled = y[labeled_idx]

for i in range(10):
    
    model = LogisticRegression()
    model.fit(X_labeled, y_labeled)
    
    probs = model.predict_proba(X[unlabeled_idx])
    
    uncertainty = np.abs(probs[:, 1] - 0.5)
    query_index = np.argmin(uncertainty)
    
    selected_sample = unlabeled_idx[query_index]
    
    labeled_idx.append(selected_sample)
    unlabeled_idx.remove(selected_sample)
    
    X_labeled = X[labeled_idx]
    y_labeled = y[labeled_idx]
    
    print(f"Iteration {i+1}: Labeled dataset size = {len(labeled_idx)}")
