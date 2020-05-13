import random
from abc import ABC, abstractmethod

#DO NOT CHANGE THIS CLASS: EXTEND IT WITH YOUR OWN
class AgentRandom():

    def __init__(self):
        super().__init__()
        #self.model = model

    def run(self, env):
        #self.model.reset()
        episodios = []
        for i in range(500):
            state = random.choice(env.states)
            #print(state)
            env.reset(state)
            episodio = self.loop(env)
            episodios.append(episodio)
        print(episodios)

    def loop(self, env):
        print("Agente random...")
        episodio = []
        done = env.end()
        while not done:  
            initialState = env.current_state
            actions = env.posibleActions()
            action = random.choice(actions)
            current_state,reward = env.step(action)
            subEpisodio = (initialState,action,current_state,reward)
            episodio.append(subEpisodio)

            done = env.end()
        return episodio

