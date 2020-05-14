from .model import Model

class DogModel(Model):
    def __init__(self):
        actions = ['buscar','perseguir','atrapar','festejar','jugar']
        states = ['rutina','perseguir_lejos','perseguir_cerca','aptrapado','despistado','fin_robo']
        T_R = dict()
        T_R[('rutina','jugar','rutina')] = (99/100,1)
        T_R[('rutina','buscar','rutina')] = (2/5,-1)
        T_R[('rutina','buscar','perseguir_lejos')] = (3/5,0)
        T_R[('rutina','jugar','fin_robo')] = (1/100,-500)
        T_R[('perseguir_lejos','perseguir','perseguir_lejos')] = (7/10,-1)
        T_R[('perseguir_lejos','atrapar','atrapado')] = (1/10,0)
        T_R[('perseguir_lejos','atrapar','despistado')] = (9/10,-10)
        T_R[('perseguir_lejos','perseguir','perseguir_cerca')] = (3/10,-1)
        T_R[('perseguir_cerca','atrapar','despistado')] = (2/7,-10)
        T_R[('perseguir_cerca','atrapar','atrapado')] = (5/7,0)
        T_R[('despistado','buscar','perseguir_lejos')] = (4/8,0)
        T_R[('despistado','buscar','despistado')] = (1/8,-2)
        T_R[('despistado','buscar','fin_robo')] = (3/8,-10)
        T_R[('atrapado','festejar','fin_robo')] = (1,20)
        super().__init__(actions, states, T_R)

    def is_final_state(self, state):
        if(state == 'fin_robo'):
            return True
        else:
            return False