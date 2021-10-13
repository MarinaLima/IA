"""
Agente conhece só os vizinhos
Agente recebe quais posições ele pode visitar baseado no ponto inicial
    0 livre 1 ocupado

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
            if (0 <= position[0] <= self.map.shape[0]) and (0 <= position[1] <= self.map.shape[1]) and \
                    map[position[0]][position[1]] == 0:
                available.append(position)
        return available

    def initial_percepts(self):
        available = self.get_available_positions(self.start)

        return [{'available_actions': available,
                'position': self.agent_position}]

    def signal(self, action):
        """
            Recebe ação e retorna novo conjuntio de percepções
            Agente que decide qual posição ele vai
        """
        self.agent_position += action['step']

        available = self.get_available_positions(self.agent_position)

        return [{'available_actions': available,
                 'position': self.agent_position}]


if __name__ == '__main__':
    map = [[0, 1],
           [1, 0]]
