import numpy as np

class Agent():

    def __init__(self, policy):
        self.policy = policy

    def run(self, env, initialState):
        env.reset(initialState)
        return self.loop(env)

    def loop(self, env):
        episode = []
        done = env.end()
        while not done: 
            initialState = env.current_state
            actions = env.posibleActions()
            action = self.policy.action(actions)
            current_state,reward = env.step(action)
            subEpisode = (initialState,action,current_state,reward)
            episode.append(subEpisode)
            done = env.end()
        return episode
