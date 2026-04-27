import numpy as np
import gymnasium as gym

def td_learning(env, episodes=500, alpha=0.1, gamma=0.9):
    v = np.zeros(env.observation_space.n)
    
    for ep in range(episodes):
        state, _ = env.reset()
        done = False
        truncated = False
        
        while not (done or truncated):
            action = env.action_space.sample()
            
            next_state, reward, done, truncated, _ = env.step(action)
        
            td_target = reward + gamma * v[next_state]
            v[state] += alpha * (td_target - v[state])
            
            state = next_state
            
    return v


env = gym.make('FrozenLake-v1', is_slippery=False)

print("====    Temporal Difference Output    ======")
v_td = td_learning(env)

for i, val in enumerate(v_td):
    print(f"State {i}: {val:.4f}")
    
print("\nGrid View")
print(v_td.reshape(4, 4))
