import numpy as np

from .policy import Policy
from Models.model import Model

class PolicyIteration(Policy):

    def __init__(self, model):
        super().__init__()
        self.model = model
        self.states = model.get_all_states()
        self.V = dict()
        for s in self.states:
            self.V[s] = 0

        #hardcodeado
        self.policy = dict()
        for s in self.states:
            if(not self.model.is_final_state(s)):
                self.policy[s] = model.posible_actions(s)[0]
        #borro el ultimo estado porque genera problemas al no tener acciones posibles
        self.states.remove('fin_robo')
        self.policy_iteration(self.policy, 0.05, self.V)

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

    def policy_evaluation(self, policy, theta, V):
        done = False
        while not done:
            delta = 0
            for s in self.states:
                V_old = V[s]
                V[s] = self.Q(s, policy[s], V)
                delta = max(delta, abs(V_old - V[s]))
            done = delta < theta
        return V

    def policy_iteration(self, policy, theta, V):
        V = self.policy_evaluation(policy, theta, V)
        done = False
        while not done:
            stable = True
            for s in self.states:
                action_old = policy[s]
                actions = self.model.posible_actions(s)
                all_Qs = [self.Q(s, a , V) for a in actions]
                policy[s] = actions[np.argmax(all_Qs)]
                if(action_old != policy[s]):
                    stable = False
            if not stable: 
                V = self.policy_evaluation(policy, theta, V)
            else:
                done = True
        return policy, V
    