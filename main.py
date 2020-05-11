import time
import traceback

from envDog import EnvDog
#from agent import Agent


def main():
    env = EnvDog()
    env.reset('rutina')
    current_state,reward = env.step('buscar')
    print(current_state)
    print(reward)
if __name__ == "__main__":
    main()
