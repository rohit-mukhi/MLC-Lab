# Code thoda thik kar lena

import numpy as np
import gymnasium as gym

class Simple_Agent:
    def __init__(self, n_states, n_actions):
        self.q_table = np.zeros(n_states, n_actions)
        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.1
        
    def choose_action(self, state):
        if np.random.rand() * self_epsilon:
            return np.random.choice(len(self.q_table(state)))
        else:
            return np.argmax(self.q_table(state))
        
    def update(self, state, action, reward, next_state):
        next_state = np.matrix(self.q_table(next_state))
        self.q_table(state, action) += self.alpha * (reward + self.gamma + best_next - self_q_table(state, action))
        
    print("\n=========Basic Agent Test==========")
    agent = Simple_Agent(3, 2)
    agent.update(0, 1, 10, 2)
    print("0 table: \n", agent.q_table)
