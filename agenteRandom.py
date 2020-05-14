import random
import numpy as np
from graphviz import Digraph
from abc import ABC, abstractmethod

#DO NOT CHANGE THIS CLASS: EXTEND IT WITH YOUR OWN
class AgentRandom():

    def __init__(self):
        super().__init__()
        #self.model = model

    def run(self, env):
        #self.model.reset()
        episodios = []
        for i in range(800):
            state = random.choice(env.states)
            #print(state)
            env.reset(state)
            episodio = self.loop(env)
            episodios.append(episodio)
        #print(episodios)

        episodios10 = self.episodiosPorCantidad(episodios,10)
        T_R = dict()
        T_R = self.MDPMonteCarlo(episodios10,env)
        self.render(T_R,"graf 10")

        episodios100 = self.episodiosPorCantidad(episodios,100)
        T_R = dict()
        T_R = self.MDPMonteCarlo(episodios10,env)
        self.render(T_R,"graf 100")

        episodios800 = self.episodiosPorCantidad(episodios,800)
        T_R = dict()
        T_R = self.MDPMonteCarlo(episodios800,env)
        self.render(T_R,"graf 800")

    def render(self,T_R,name):
        g = Digraph(filename=name)
        for (s1,a,s2), (T,R) in T_R.items():
            g.edge(s1,s2,str(a) + ", "+str(T) + ", "+str(R))
        g.view()
        print('----------------------')
        print(T_R)
        print('----------------------')

    def loop(self, env):
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
        T_R = dict()
        for n in nodos:
            s0 = n[0]
            a = n[1]
            s1 = n[2]
            count_s_a_s = 0
            count_s_a = 0
            reward = 0
            for e in episodios:
                if(e[0] == s0 and e[1] == a):
                    count_s_a += 1
                    if(e[2] == s1):
                        reward = reward + e[3]
                        count_s_a_s += 1
            T = count_s_a_s / count_s_a
            R = reward / count_s_a_s
            T_R[(s0,a,s1)] = (T,R)
        return T_R
                    

    def episodiosPorCantidad(self,episodios,cantidad):
        lista = []
        for i in range(cantidad):
            episodio = episodios[i]
            for sus in episodio:
                lista.append(sus)
        return lista
