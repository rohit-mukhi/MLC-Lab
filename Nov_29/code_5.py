from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=200)

rfe = RFE(model, n_features_to_select=2)
fit = rfe.fit(x, y)

print("Selected features: ", fit.support_)
print("Feature Ranking: ", fit.ranking_)
