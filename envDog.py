import numpy as np
import gym
import random
from gym import error, spaces, utils



class EnvDog(gym.Env):


    def __init__(self):
        self.actions = ['buscar','perseguir','atrapar','festejar','jugar']
        self.states = ['rutina','perseguir_lejos','perseguir_cerca','aptrapado','despistado','fin_robo']
        self.current_state = ''
        self.T_R = dict()
        self.T_R = self.MDP(self.T_R)
        

        #self.render()
    def MDP(self,T_R):
        T_R[('rutina','jugar','rutina')] = (99/100,1)
        T_R[('rutina','buscar','rutina')] = (2/5,-1)
        T_R[('rutina','buscar','perseguir_lejos')] = (3/5,0)
        T_R[('rutina','jugar','fin_robo')] = (1/100,-500)
        T_R[('perseguir_lejos','perseguir','perseguir_lejos')] = (7/10,-1)
        T_R[('perseguir_lejos','atrapar','aptrapado')] = (1/10,0)
        T_R[('perseguir_lejos','atrapar','despistado')] = (9/10,-10)
        T_R[('perseguir_lejos','perseguir','perseguir_cerca')] = (3/10,-1)
        T_R[('perseguir_cerca','atrapar','despistado')] = (2/7,-10)
        T_R[('perseguir_cerca','atrapar','aptrapado')] = (5/7,0)
        T_R[('despistado','buscar','perseguir_lejos')] = (4/8,0)
        T_R[('despistado','buscar','despistado')] = (1/8,-2)
        T_R[('despistado','buscar','fin_robo')] = (3/8,-10)
        T_R[('aptrapado','festejar','fin_robo')] = (1,20)
        return T_R

    def end(self):
        if (self.current_state == 'fin_robo'):
            return True
        else:
            return False

    def posibleActions(self):
        actionsReturn = []
        for action in self.actions:
            for stateAux in self.states:
                val = self.T_R.get((self.current_state,action,stateAux))
                if( not(val == None)):
                    if(not (action in actionsReturn)):
                        actionsReturn.append(action)
        print(actionsReturn)
        return actionsReturn



    def step(self, action):
        next_states, probas = self.get_next_states(self.current_state,action)
        choice = random.choices(next_states,probas)
        self.current_state, reward = choice[0][0], choice[0][1]

        return self.current_state,reward

    def reset(self,initial_state):
        self.current_state = initial_state
        return self.current_state

    def get_next_states(self,current_state,action):
        next_states = []
        probas =[]
        for state in self.states:
            val = self.T_R.get((current_state,action,state))
            if( not(val == None)):
                next_states.append((state,val[1]))
                probas.append(val[0])
        return next_states, probas

    #def is_game_over(self):


    #def render(self, mode="human", close=False):

    #def __del__(self):


    #def _configure(self, display=None):


    #def _seed(self, seed=None):



