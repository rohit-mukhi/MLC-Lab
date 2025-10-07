import numpy as np

outcomes = np.array([0, 0])
for val in range(1, 1001):
    outcome = np.random.randint(0, 2)
    outcomes[outcome] = outcomes[outcome] + 1

print(f"Head occured: {outcomes[1]} times")
print(f"Tail occured: {outcomes[0]} times")

probability_of_head = (outcomes[1]/1000) * 100
print(f"Probabiltiy of getting head is: {probability_of_head}%")
