import random
from abc import ABC, abstractmethod

#DO NOT CHANGE THIS CLASS: EXTEND IT WITH YOUR OWN
class AgentRandom():

    def __init__(self):
        super().__init__()
        #self.model = model

    def run(self, env):
        #self.model.reset()
        self.loop(env)

    def loop(self, env):
        print("Agente random...")
        #obs = env.reset()
        #env.render()
        episodios = []
        done = False
        while not done:  
            initialState = env.current_state
            actions = env.posibleActions()
            action = random.choice(actions)
            current_state,reward = env.step(action)
            episodio = (initialState,action,current_state,reward)
            episodios.append(episodio)

            done = env.end()
        print('episodios: ',episodios)

