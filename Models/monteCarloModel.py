from .model import Model

class MonteCarloModel(Model):
    def __init__(self, episodes):
        actions = ['buscar','perseguir','atrapar','festejar','jugar']
        states = ['rutina','perseguir_lejos','perseguir_cerca','atrapado','despistado','fin_robo']
        T_R = self.__monte_carlo_model_estimation(episodes)
        super().__init__(actions, states, T_R)

    def is_final_state(self, state):
        if(state == 'fin_robo'):
            return True
        else:
            return False

    def __monte_carlo_model_estimation(self,episodes):
        nodes = []
        for episode in episodes:
            for seq in episode:
                if(not seq in nodes):
                    nodes.append(seq)
        T_R = dict()
        for n in nodes:
            s0 = n[0]
            a = n[1]
            s1 = n[2]
            count_s_a_s = 0
            count_s_a = 0
            reward = 0
            for episode in episodes:
                for seq in episode:
                    if(seq[0] == s0 and seq[1] == a):
                        count_s_a += 1
                        if(seq[2] == s1):
                            reward = reward + seq[3]
                            count_s_a_s += 1
            T = count_s_a_s / count_s_a
            R = reward / count_s_a_s
            T_R[(s0,a,s1)] = (T,R)
        return T_R