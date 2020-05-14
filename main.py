import time
import traceback

from Environments.environment import Environment
from Agents.policy_based_agent import Agent
from Policies.randomPolicy import RandomPolicy
from Models.monteCarloModel import MonteCarloModel
from Models.dogModel import DogModel

def main():
    #1
    dog_model = DogModel()
    env = Environment(dog_model)

    #2
    random_agent = Agent(RandomPolicy())
    episode = random_agent.run(env, 'rutina')

    #3
    episodes_10 = generate_episodes(10, random_agent, env, 'rutina')
    episodes_100 = generate_episodes(100, random_agent, env, 'rutina')
    episodes_500 = generate_episodes(500, random_agent, env, 'rutina')

    #render modelo original
    dog_model.render('DogModel')
    #render modelos estimados por montecarlo
    MDPMonteCarlo = MonteCarloModel(episodes_10)
    MDPMonteCarlo.render('MC10')
    MDPMonteCarlo = MonteCarloModel(episodes_100)
    MDPMonteCarlo.render('MC100')
    MDPMonteCarlo = MonteCarloModel(episodes_500)
    MDPMonteCarlo.render('MC500')

    #4

def generate_episodes(episodes_quantity, agent, environment, initial_state):
    episodes = []
    for i in range(episodes_quantity):
        episodes.append(agent.run(environment, initial_state))
    return episodes

if __name__ == "__main__":
    main()
