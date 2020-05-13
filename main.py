import time
import traceback

from envDog import EnvDog
from agenteRandom import AgentRandom
#from agent import Agent


def main():
    env = EnvDog()
    #env.reset('rutina')
    agente = AgentRandom()
    agente.run(env)
    #random de acciones de ambiente
    #actions = env.posibleActions()
    #current_state,reward = env.step('atrapar')
    #print(current_state)
    #print(reward)
if __name__ == "__main__":
    main()
