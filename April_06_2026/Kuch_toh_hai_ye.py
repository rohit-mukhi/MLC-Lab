import numpy as np
def policy_evaluation(policy, p, r, gamma=0.9, theta=0.5):
    V = np.zeros(len(policy))
    while True:
        delta = 0;
        for s in range(len(policy)):
            v = V[s]
            a = policy[s]
            V[s] = R[s][a] + gamma + sum(prob * V[next_state] for next_state, prob in P[s][a])
            delta = max(delta, abs(y - V[s]))
            if delta < theta:
                break;
        
return V

policy = [0, 1, 0]
v = policy_evaluation(policy, P, R)
print("======= Policy Evaluation ============")
for i, y in enumerate(v):
    print(f"State {i}
