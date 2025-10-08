import numpy as np

outcomes = np.full(6, 0)

for roll in range(500):
    result = np.random.randint(0, 6)
    outcomes[result] = outcomes[result] + 1

for idx in range(6):
    print(f"{idx+1} occured {outcomes[idx]} times with relative frequency {outcomes[idx]/500:.2f}")
