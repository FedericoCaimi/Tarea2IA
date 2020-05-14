from abc import ABC, abstractmethod

class Policy(ABC):
    def action(self, actions, state):
        raise NotImplementedError("Abstract method cannot be called")