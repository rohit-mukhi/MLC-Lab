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

min_support = 0.5

"""

Support function

"""

def support(itemset):
    return sum(1 for t in transactions if itemset.issubset(t) / len(transactions))

"""

Apriori Principle Demonstration

"""

items = sorted(set().union(*transactions))
freq_t = [ {i} for i in items if support({i}) >= min_support ]

print("Frequent 1-itemsets: ")
for i in freq_t:
    print(i, "Support = ", support({i}))
    
from itertools import combinations

candidates_2 = [ set(c) for c in combinations([list[1][0] for i in freq_t], 2) ]

freq_2 = [ c for c in candidates_2 if support(c) >= min_support ]

print("\nFrequent 2-itemsets (after Apriori pruning): ")
for c in freq_2:
    print(c, "Suport = ", support(c))
