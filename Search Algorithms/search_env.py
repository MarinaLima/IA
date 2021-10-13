"""
Agente conhece só os vizinhos
Agente recebe quais posições ele pode visitar baseado no ponto inicial
    0 livre 1 ocupado
Implementar interface gráfica
Implementar um ambiente dinâmico - que muda o objetivo

"""
import numpy as np


class Environment:

    def __init__(self, map, start, goal):
        self.map = np.array(map)
        self.start = np.array(start)
        self.goal = np.array(goal)
        self.agent_position = np.array(start)
        # Ações possiveis do agente: pode andar pra frente, pra trás, pra cima, para baixo, na diagonal
        self.actions = np.array([[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]])

    def get_available_positions(self, initial_position):
        available = []
        # Passa pro agente apenas as ações possiveis, baseadas no mapa
        for a in self.actions:
            position = initial_position + a
            # Verifica se a posição está disponível e se está dentro dos limites do mapa
            if (0 <= position[0] < self.map.shape[0]) and (0 <= position[1] < self.map.shape[1]) and \
                    map[position[0]][position[1]] == 0:
                available.append(position)
        return available

    def initial_percepts(self):
        available = self.get_available_positions(self.start)

        return {'available_positions': available,
                'position': self.agent_position,
                'goal': self.goal}

    def signal(self, action):
        """
            Recebe ação e retorna novo conjuntio de percepções
            Agente que decide qual posição ele vai
        """
        self.agent_position = action['step']

        available = self.get_available_positions(self.agent_position)

        return {'available_positions': available,
                'position': self.agent_position,
                'goal': self.goal}


class AgentBFS:
    """
        Busca em largura - sempre encontra o caminho com menor número de arestas possíveis
    """

    def __init__(self, env):
        self.belief_state = env.initial_percepts()
        self.environment = env

    def act(self):
        """
        Faz a ação - algoritmo de busca
        """
        # Começa com uma fronteira com o estado inicial, guarda as posições
        # Vai ter vºárias posições e caminhos
        f = [[self.belief_state['position']]]

        # Enquanto a fornteira não estiver vazia
        while f:
            # A gente tira um caminho do início da fronteira
            path = f.pop(0)
            # Visita o nó
            self.belief_state = self.environment.signal({'step': path[-1]})
            # Verifica se é a posição final
            if (path[-1] == self.belief_state['goal']).all():
                return path
            # Visita posição e verifica ações possiveis
            else:
                for p in self.belief_state['available_positions']:
                    # Busca em largura - adiciona no final da fila as posições disponíveis
                    f.append(path + [p])


if __name__ == '__main__':
    map = [[0, 0, 1],
           [1, 0, 1],
           [1, 0, 0]]

    env = Environment(map, [0, 0], [2, 2])

    ag = AgentBFS(env)
    path = ag.act()
    print(path)

