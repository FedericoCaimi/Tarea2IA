import time
import traceback
import random

from Environments.environment import Environment
from Agents.policy_based_agent import Agent
from Policies.randomPolicy import RandomPolicy
from Policies.policy_iteration import PolicyIteration
from Policies.value_iteration import ValueIteration
from Models.monteCarloModel import MonteCarloModel
from Models.dogModel import DogModel

def main():
    #1
    dog_model = DogModel()
    env = Environment(dog_model)

    #2
    random_agent = Agent(RandomPolicy())

    #3
    episodes_10 = generate_episodes(10, random_agent, env)
    episodes_100 = generate_episodes(100, random_agent, env)
    episodes_500 = generate_episodes(500, random_agent, env)
    episodes_1000 = generate_episodes(1000, random_agent, env)
    #render modelo original
    dog_model.render('DogModel')
    
    #render modelos estimados por montecarlo
    MDPMonteCarlo = MonteCarloModel(episodes_10)
    MDPMonteCarlo.render('MC10')
    MDPMonteCarlo = MonteCarloModel(episodes_100)
    MDPMonteCarlo.render('MC100')
    MDPMonteCarlo = MonteCarloModel(episodes_500)
    MDPMonteCarlo.render('MC500')
    MDPMonteCarlo = MonteCarloModel(episodes_1000)
    MDPMonteCarlo.render('MC1000')

    #4
    print('--------------------------------')
    policy_it = PolicyIteration(MDPMonteCarlo)
    print('Policy iteration con Montecarlo: ',str(policy_it))
    print('--------------------------------')

    print('--------------------------------')
    policy_value_it = ValueIteration(MDPMonteCarlo)
    print('Policy value iteration con Montecarlo: ',str(policy_value_it))
    print('--------------------------------')

    print('--------------------------------')
    policy_it_DogM = PolicyIteration(dog_model)
    print('Policy iteration con MDP real: ',str(policy_it_DogM))
    print('--------------------------------')

    print('--------------------------------')
    policy_value_it_DogM = ValueIteration(dog_model)
    print('Policy value iteration con MDP real: ',str(policy_value_it_DogM))
    print('--------------------------------')

    #5
    improved_agent = Agent(policy_it)
    episode, reward = improved_agent.run(env, 'rutina')
    print("Agente Policy Iteration:")
    print('Episodio:', episode)
    print('Recompensa:', reward)
    print('--------------------------------')

    improved_agent = Agent(policy_value_it)
    episode, reward = improved_agent.run(env, 'rutina')
    print("Agente Value Iteration:")
    print('Episodio:', episode)
    print('Recompensa:', reward)
    print('--------------------------------')

    #Evaluando politicas
    r_random, r_policy_it, r_value_it = recompensa_media(1000, RandomPolicy(), policy_it, policy_value_it, env)
    print('Recompensa media random policy:', r_random)
    print('Recompensa media policy iteration:', r_policy_it)
    print('Recompensa media value iteration:', r_value_it)

def generate_episodes(episodes_quantity, agent, environment):
    states = ['rutina','perseguir_lejos','perseguir_cerca','atrapado','despistado','fin_robo']
    episodes = []
    for i in range(episodes_quantity):
        e, r = agent.run(environment, random.choice(states))
        episodes.append(e)
    return episodes

def recompensa_media(number_of_runs, random_policy, policy_it, value_it, env):
    reward_random = 0
    reward_policy_it = 0
    reward_value_it = 0
    for i in range(number_of_runs):
        agent = Agent(random_policy)
        episode, reward = agent.run(env, 'rutina')
        reward_random = reward_random + reward

        agent = Agent(policy_it)
        episode, reward = agent.run(env, 'rutina')
        reward_policy_it = reward_policy_it + reward

        agent = Agent(value_it)
        episode, reward = agent.run(env, 'rutina')
        reward_value_it = reward_value_it + reward
    return reward_random/number_of_runs, reward_policy_it/number_of_runs, reward_value_it/number_of_runs


if __name__ == "__main__":
    main()
