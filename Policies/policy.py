from abc import ABC, abstractmethod

class Policy(ABC):
    def action(self, actions):
        raise NotImplementedError("Abstract method cannot be called")