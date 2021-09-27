"""
    Controle de Papel Higiênico:
    + Ambiente
        - Número de rolos existentes (estoque)
        - Modelo de gasto: média e desvio padrão por dia (amostragem aleatória com distribuição normal/gaussiana -
        números perto da média tem mais chances de serem gerados)
        - Modelo de preço
            - Custo Médio: $1,20 por rolo
            - Variação média: $0,20
            - Promoções: 2 vezes por mês
        - Percepções (que o ambiente envia pro agente):
            - Preço
            - Número de rolos no estoque

    + Agente
        - Estado de crença:
            - Preço bom
            - Estoque baixo
        - Agir (método)
            - Adicionar rolos no estoque
            - Adicionar despesa ($) à conta - nunca fica sem dinheiro, mas a meta é gastar o mínimo possivel
        - Lembrar
            - Atualizar a noção de preço bom
            - Atualizar a noção de estoque baixo

    - analisar como o agente sairia com a mudança do modelo de preço e estoque
"""


class Environment:

    def __init__(self):
        pass

    def initial_percepts(self):
        return {'n': x, 'price': p}

    def signal(self, action):
        return {'n': x, 'price': p}


class Agent:

    def __init__(self, environment):
        self.environment = environment
        self.percepts = environment.initial_percepts()
        self.S = {'cheap': self.percepts['price'], 'low': 0}

    def act(self):
        """
        Verifies env's state
        baseado nas percepções ele executa uma ação, adicionando rolos no estoque e o valor que gastou
        """
        action = {'buy_n': n}
        percepts = self.environment.signal(action)

    def run(self, n):
        # Execute action n times
        # Guardando preço ao longo do tempo, número de rolos ao longo do tempo, gasto e plota depois
        pass


if __name__ == '__main__':
    Agent.run(5)
