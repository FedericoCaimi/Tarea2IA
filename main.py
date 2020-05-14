import time
import traceback

from Environments.envDog import EnvDog
from Agents.policy_based_agent import Agent
from Policies.randomPolicy import RandomPolicy
from Models.monteCarloModel import MonteCarloModel

def main():
    #1
    env = EnvDog()
    
    #2
    random_agent = Agent(RandomPolicy())
    episode = random_agent.run(env, 'rutina')

    #3
    episodes_10 = generate_episodes(10, random_agent, env, 'rutina')
    episodes_100 = generate_episodes(100, random_agent, env, 'rutina')
    episodes_500 = generate_episodes(500, random_agent, env, 'rutina')
    MDPMonteCarlo = MonteCarloModel(episodes_10)
    MDPMonteCarlo.render('MC10')
    MDPMonteCarlo = MonteCarloModel(episodes_100)
    MDPMonteCarlo.render('MC100')
    MDPMonteCarlo = MonteCarloModel(episodes_500)
    MDPMonteCarlo.render('MC500')

def generate_episodes(episodes_quantity, agent, environment, initial_state):
    episodes = []
    for i in range(episodes_quantity):
        episodes.append(agent.run(environment, initial_state))
    return episodes

if __name__ == "__main__":
    main()
