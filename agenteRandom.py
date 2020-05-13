import random
import numpy as np
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
        #print(episodios)

        episodios10 = self.episodiosPorCantidad(episodios,10)
        print('episodios10: ',episodios10)

        self.MDPMonteCarlo(episodios10,env)

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
    
    def MDPMonteCarlo(self,episodios,env):
        nodos = list(set(episodios))
        print('nodos: ',nodos)
        for n in nodos:
            s1 = n[0]
            a = n[1]
            s2 = n[2]
            r = n[3]
            #for s in env.states:
                #cantidad = episodios.count((s1,a,s,))
                #print(cantidad)
                    

    def episodiosPorCantidad(self,episodios,cantidad):
        lista = []
        for i in range(cantidad):
            episodio = episodios.pop()
            for sus in episodio:
                lista.append(sus)
        return lista
