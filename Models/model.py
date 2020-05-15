from abc import ABC, abstractmethod
import random
import time
from graphviz import Digraph

class Model(ABC):
    def __init__(self, actions, states, dictionary):
        self.actions = actions
        self.states = states
        self.T_R = dictionary

    def posible_actions(self, state):
        actionsReturn = []
        for action in self.actions:
            for stateAux in self.states:
                val = self.T_R.get((state,action,stateAux))
                if( not(val == None)):
                    if(not (action in actionsReturn)):
                        actionsReturn.append(action)
        return actionsReturn
    
    def step(self, state, action):
        self.check_action(action)
        next_states = []
        probabilities = []
        for next_state in self.states:
            val = self.T_R.get((state,action,next_state))
            if(not(val == None)):
                next_states.append((next_state,val[1]))
                probabilities.append(val[0])
        choice = random.choices(next_states,probabilities)
        next_state, reward = choice[0][0], choice[0][1]
        return next_state, reward

    #returns [(state, prob, reward)]
    def posible_states(self, state, action):
        self.check_action(action)
        _return = []
        for next_state in self.states:
            val = self.T_R.get((state,action,next_state))
            if(not(val == None)):
                _return.append((next_state, val[0], val[1]))
        return _return

    def is_final_state(self, state):
        raise NotImplementedError("Abstract method cannot be called")

    def check_action(self, action):
        if action not in self.actions:
            raise ValueError("Invalid Action")

    def render(self,name):
        g = Digraph(filename=name)
        for (s1,a,s2), (T,R) in self.T_R.items():
           g.edge(s1,s2,str(a) + ", "+str(T) + ", "+str(R))
        g.view()
        print('----------------------')
        print(self.T_R)
        print('----------------------')

    def get_all_states(self):
        return list(self.states)