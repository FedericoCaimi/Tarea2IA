import numpy as np
import gym
import random
from gym import error, spaces, utils
from Models.dogModel import DogModel

class Environment(gym.Env):
    def __init__(self, model):
        self.model = model
        self.current_state = ''

    def end(self):
        return self.model.is_final_state(self.current_state)

    def posibleActions(self):
        return self.model.posible_actions(self.current_state)

    def step(self, action):
        self.current_state, reward = self.model.step(self.current_state, action)
        return self.current_state, reward

    def reset(self,initial_state):
        self.current_state = initial_state
        return self.current_state

    #def is_game_over(self):


    #def render(self, mode="human", close=False):

    #def __del__(self):


    #def _configure(self, display=None):


    #def _seed(self, seed=None):



