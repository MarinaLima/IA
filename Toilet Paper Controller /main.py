"""
    Controle de Papel Higiênico:
    + Ambiente
        - Número de rolos existentes (estoque)
        - Modelo de gasto: média e desvio padrão por dia da semana (amostragem aleatória com distribuição
        normal/gaussiana)
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

import numpy as np
import matplotlib.pyplot as plt


class Environment:

    def __init__(self, n, price):
        self.n = n
        self.price = price
        self.clock = 0
        self.day = 0
        # uso de rolos de papel higiênico por dia de semana
        self.mu_usage = [10, 100, 150, 300, 125, 50, 15]
        # desvio padrão de uso
        self.sigma_usage = [2, 10, 10, 20, 10, 10, 2]
        self.mu_price = 1.2
        self.sigma_price = 0.2
        self.on_sale = False
        self.max_n = 1000

    def initial_percepts(self):
        return {'n': self.n, 'price': self.price, 'max_n': self.max_n}

    def signal(self, action):
        usage = int(np.random.normal(self.mu_usage[self.clock % len(self.mu_usage)],
                                     self.sigma_usage[self.clock % len(self.sigma_usage)]))
        bought = action['to_buy']
        self.n = self.n - usage + bought
        self.day += 1

        # no começo de cada semana verifica se tem promoção ou não
        if self.clock % 7 == 0:
            self.day = 0
            self.price = 1.2
            self.on_sale = True if np.random.rand() < 0.5 else False

            if self.on_sale:
                self.price -= self.sigma_price
            else:
                self.price = max(np.random.normal(self.mu_price, self.sigma_price), 0.9)

        self.clock += 1
        return {'n': self.n, 'price': self.price, 'max_n': self.max_n, "day": self.day}


class Agent:

    def __init__(self, environment):
        self.environment = environment
        self.percepts = environment.initial_percepts()
        self.spendings = []
        self.clock = 1
        self.S = {
            'average_price': self.percepts['price'],
            'cheap': self.percepts['price'],
            'low': 0,
            'min': self.percepts['max_n']
        }

    def act(self):
        """
        Verifies env's state
        baseado nas percepções ele executa uma ação, adicionando rolos no estoque e o valor que gastou
        """
        # Define to_buy
        to_buy = 0
        # se a quantidade está baixa compra o mínimo
        if self.percepts['n'] <= self.S['low']:
            to_buy = self.S['min'] - self.percepts['n']
        # se tá barato enche o estoque
        if self.percepts['price'] <= self.S['cheap']:
            to_buy = self.percepts['max_n'] - self.percepts['n']

        action = {'to_buy': to_buy}

        # Act
        self.spendings.append(to_buy * self.percepts['price'])
        self.percepts = self.environment.signal(action)

        # Update belief state
        mean_value = (self.S['average_price'] * self.clock + self.percepts['price']) / (self.clock + 1)

        self.S = {
            'average_price': mean_value,
            # TODO mudar o multiplicador, fica verificando se preço baixo acontece, se não tiver preço baixo por muito tempo aumenta ele até chegar na média
            # ou o barato pode ser menor que a última compra
            # 'cheap': mean_value * 0.8,
            'cheap': self.percepts['price'],
            'low': self.environment.mu_usage[self.percepts['day']],
            'min': self.environment.mu_usage[self.percepts['day']] * 1.5
        }
        self.clock += 1


if __name__ == '__main__':
    env = Environment(0, 1.2)
    ag = Agent(env)

    prices = []
    inventory = []
    days = 1000

    for i in range(days):
        ag.act()
        prices.append(env.price)
        inventory.append(env.n)

    # fig, ax1 = plt.subplots()
    # ax2 = ax1.twinx()
    # ax1.plot(prices, 'g-')
    # ax2.plot(inventory, 'b-')

    # ax1.set_xlabel('Tempo')
    # ax1.set_ylabel("Preço", color='g')
    # ax2.set_ylabel("Estoque", color='b')

    plt.plot(prices)
    plt.title("Preço")
    plt.show()

    plt.plot(inventory)
    plt.title("Estoque")
    plt.show()

    plt.plot(ag.spendings)
    plt.title("Gastos")
    plt.show()

    plt.show()

"""
    plt.plot(prices, label="Preço")
    plt.plot(inventory, label="Estoque")
    plt.plot(ag.spendings, label="Gasto")
    plt.legend()
 """

