import numpy as np
import gymnasium as gym

def q_learning(env, episodes=2000, alpha=0.1, gamma=0.9, epsilon=0.1):
    n_states = env.observation_space.n
    n_actions = env.action_space.n
    Q = np.zeros((n_states, n_actions))
    
    for ep in range(episodes):
        state, info = env.reset()
        done = False
        
        while not done:
            if np.random.rand() < epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(Q[state])
                
            step_result = env.step(action)
            next_state, reward, terminated, truncated = step_result[:4]
            
            done = terminated or truncated
            
            best_next_action = np.argmax(Q[next_state])
            
            td_target = reward + gamma * Q[next_state][best_next_action] * (not terminated)
            
            td_error = td_target - Q[state][action]
            Q[state][action] += alpha * td_error
            
            state = next_state
            
    return Q

env = gym.make("Taxi-v3")

print("Training agent...")
trained_q_table = q_learning(env, episodes=2000)
print("Training complete!")

print("\nSample of the learned Q-Table (First 5 states):")
print(trained_q_table[:5])
