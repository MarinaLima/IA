"""
    Criar uma população de indivíduos
    - Seleção
        Função Fitness
    - Mutação
    - Cruzamento

    Algoritmo estocástico - para a mesma entrada pode ter saídas diferentes - precisa rolar várias vezes
"""
import copy as cp
import numpy as np
import matplotlib.pyplot as plt


def fitness(ind):
    """
    Recebe indivíduo e verifica o quão adaptado ele está ao ambiente
    ind = [1,1,3,4] -> Vetor indicando a coluna em que cada rainha está
    Verifica conflitos e retorna o negativo desse valor - quanto maior o fitness mais adap-tado o indivíduo está
    """
    conflicts = 0

    for i in range(len(ind)):
        for j in ind:
            # se tiver duas rainhas na mesma coluna
            if i != j:
                if ind[i] == ind[j]:
                    conflicts += 1
                # para verificar se está na mesma diagonal verica se a diferença entre o índice das linhas (dy) e das
                # colunas (dx) são iguais
                if abs(ind[i] - ind[j]) == abs(i - j):
                    conflicts += 1

    return -conflicts


def mutation(ind):
    """
    Gera alteração aleatória no indivíduo
    """
    _ind = cp.copy(ind)
    n = len(ind)

    queen = np.random.randint(n)
    pos = np.random.randint(n)

    _ind[queen] = pos

    return _ind


def crossover(ind1, ind2):
    """
    Pode ter mais de 2 indivíduos no cruzamento
    """
    n = len(ind1)
    # pega 2 pontos de corte e retorna os dois novos invidíduos
    p1 = np.random.randint(n)
    p2 = np.random.randint(n)
    while p1 == p2:
        p2 = np.random.randint(n)

    if p1 > p2:
        p1, p2 = p2, p1

    off1 = []
    off2 = []

    for i in range(0, p1):
        off1.append(ind1[i])
        off2.append(ind2[i])

    for i in range(p1, p2):
        off1.append(ind2[i])
        off2.append(ind1[i])

    for i in range(p2, n):
        off1.append(ind1[i])
        off2.append(ind2[i])

    return off1, off2


def evolve(pop, ngen=10, prob_mut=0.05):
    """
    Todos individuos reproduzem
    """
    best_ind = []
    best_fitness = 0

    best_fit_bygen = []

    for i in range(ngen):
        newpop = []
        for ind in pop:
            off1, off2 = crossover(ind, pop[np.random.randint(len(pop))])

            # mutação é operador exclusivo de difersidade - sempre adiciona diversidade
            # cruzamento trás diversidade mas também convergência, combinando soluções boas
            if np.random.rand() < prob_mut:
                off1 = mutation(off1)

            if np.random.rand() < prob_mut:
                off2 = mutation(off2)

            champion, champion_fitness = \
                (off1, fitness(off1)) if fitness(off1) >= fitness(off2) else (off2, fitness(off2))
            # >= pra garantir que vai andar na região plana
            champion, champion_fitness = \
                (champion, champion_fitness) if fitness(champion) >= fitness(ind) else (ind, fitness(ind))

            newpop.append(champion)

            if not best_ind:
                best_ind = champion
                best_fitness = champion_fitness

            elif champion_fitness >= best_fitness:
                best_ind = champion
                best_fitness = champion_fitness

        best_fit_bygen.append(best_fitness)
        pop = newpop.copy()

    return best_fitness, best_ind, best_fit_bygen


if __name__ == '__main__':
    """
    print(fitness([1, 2, 3, 0]))
    print(fitness([1, 1, 1, 1]))
    print(mutation([1, 1, 1, 1]))
    print(crossover([1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2]))
    """
    n = 12
    popsize = 50
    pop = [[np.random.randint(n) for i in range(n)] for j in range(popsize)]
    # print(pop)
    best_fitness, best_ind, best_fit_bygen = evolve(pop, ngen=500, prob_mut=0.3)
    print(best_fitness)
    print(best_ind)
    plt.plot(best_fit_bygen)
    plt.show()
