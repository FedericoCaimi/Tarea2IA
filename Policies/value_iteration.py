import numpy as np

from .policy import Policy
from Models.model import Model

class ValueIteration(Policy):

    def __init__(self, model):
        super().__init__()
        self.model = model
        self.states = model.get_all_states()
        self.V = dict()
        for s in self.states:
            self.V[s] = 0

        #hardcodeado
        #borro el ultimo estado porque genera problemas al no tener acciones posibles
        self.states.remove('fin_robo')
        self.policy = self.value_iteration(0.001, 0.99, self.V)

    def action(self, actions, state):
        return self.policy[state]
    
    def Q(self, state, action, V, gamma=0.99):
        #states_prob_rewards type: [(state, probability, reward)]
        states_prob_rewards = self.model.posible_states(state, action)
        return np.sum([self.Q_help(state, action, s_p_r, V, gamma) for s_p_r in states_prob_rewards])
    
    def Q_help(self, state, action, state_probability_reward, V, gamma):
        T = state_probability_reward[1]
        next_s = state_probability_reward[0]
        R = state_probability_reward[2]
        return T * (R + gamma * V[next_s])

    def value_iteration(self, theta, gamma, V):
        done = False
        policy = dict()
        while not done:
            delta = 0
            for s in self.states:
                old = V[s]
                actions = self.model.posible_actions(s)
                all_Qs = [self.Q(s, a , V) for a in actions]
                V[s] = np.max(all_Qs)
                policy[s] = actions[np.argmax(all_Qs)]
                delta = max(delta, abs(old - V[s]))
            done = delta < theta
        return policy
    
    