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
"""


def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')