import pandas as pd

"""
Market Basket analysis
    Discover frequent itemsets
    Generate association rules

"""

transactions = [
    ["Bread", "Milk", "Egg", "Butter", "Salt", "Apple"],
    ["Bread", "Milk", "Egg", "Apple"],
    ["Bread", "Milk", "Butter","Apple"],
    ["Milk","Egg", "Butter", "Apple"],
    ["Bread", "Egg", "Butter","Apple"],
    ["Bread", "Egg", "Salt"],
    ["Bread","Milk","Egg","Apple"]
]

print(transactions)

items = sorted(set().union(*transactions))

data =[]

for t in transactions:
    row = {item: (1 if item in t else 0) for item in items}
    data.append(row)
    
df = pd.DataFrame(data)
df.index = range(1, len(df) + 1)
df.index.name = "Transactions"

print(df)

def support(itemset, transactions):
    return sum(1 for t in transactions if itemset.issubset(t) / len(transactions))

def confidence(X, Y, transactions):
    return support(X.union(Y), transactions) / support(X, transactions)

print("Support (Brand): ", support({"Bread"}, transactions))
print("Confidence (Bread-Milk): ", confidence({"Bread"}, {"Milk"}, transactions))
print("Confidence (Bread-Milk-Egg): ", confidence({"Bread","Milk"}, {"Egg"}, transactions))
