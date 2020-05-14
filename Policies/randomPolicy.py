import random
from .policy import Policy

class RandomPolicy(Policy):

    def __init__(self):
        super().__init__()

    def action(self, actions, state):
        return random.choice(actions)