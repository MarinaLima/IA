"""
    Controle de Papel Higiênico:
    + Ambiente
        - Número de rolos existentes (estoque)
        - Modelo de gasto: média e desvio padrão por dia da semana (amostragem aleatória com distribuição normal/gaussiana -
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
        # uso de rolos de papel higiênico por dia de semana
        self.mu_usage = [10, 100, 150, 300, 125, 50, 15]
        # desvio padrão de uso
        self.sigma_usage = [2, 10, 10, 20, 10, 10, 2]
        self.mu_price = 1.2
        self.sigma_price = 0.2
        self.on_sale = False

    def initial_percepts(self):
        return {'n': self.n, 'price': self.price}

    def signal(self, action):

        usage = np.random.normal(self.mu_usage[self.clock % len(self.mu_usage)],
                                 self.sigma_usage[self.clock % len(self.sigma_usage)])
        bought = action['to_buy']
        self.n = self.n - usage + bought

        # no começo de cada semana verifica se tem promoção ou não
        if self.clock % 7 == 0:
            self.price = 1.2
            self.on_sale = True if np.random.rand() < 0.5 else False

        if self.on_sale:
            self.mu_price -= self.sigma_price
        else:
            self.sigma_price = max(np.random.normal(self.mu_price, self.sigma_price), 0.9)

        self.price = np.random.normal(self.mu_price, self.sigma_price)

        self.clock += 1
        return {'n': self.n, 'price': self.price}


if __name__ == '__main__':
    env = Environment(0, 1.2)

    prices = []

    for i in range(1000):
        percepts = env.signal({'to_buy': 0})
        prices.append((percepts['price']))

        plt.plot(prices)
        plt.show()

        plt.hist(prices)
        plt.show

