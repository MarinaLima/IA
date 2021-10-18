"""
Agente conhece só os vizinhos
Agente recebe quais posições ele pode visitar baseado no ponto inicial
    0 livre 1 ocupado
Implementar interface gráfica
Implementar um ambiente dinâmico - que muda o objetivo

Para transformar em busca por profundidade é só adicionar no inicio da pilha, mas precisa implementar algo para não
agarrar no loop

"""
import numpy as np


class Environment:

    def __init__(self, start, goal, room=[], n=10, prob=0.3):
        """

        :param start: The position where the agents startes
        :param goal: The position ehre the agent has to go
        :param room: A matrix representing the free spaces, 0, and obstacles 1.
        :param n: size of the genrated room is a room is not given
        :param prob: prob is the probability the a given position will have an obstacle in the generated room
        """
        if not room:
            self.room = np.zeros((n, n))

            for i in range(len(self.room)):
                for j in range(len(self.room[0])):
                    self.room[i][j] = 1 if np.random.random() < prob else 0
        else:
            self.room = np.array(room)

        self.start = np.array(start)
        self.goal = np.array(goal)
        # Makes sure that the target position does not have an obstacle
        self.room[self.goal[0]][self.goal[1]] = 0
        self.agent_position = np.array(start)
        # Ações possiveis do agente: pode andar pra frente, pra trás, pra cima, para baixo, na diagonal
        self.actions = np.array([[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]])

    def get_available_positions(self, initial_position):
        available = []
        # Passa pro agente apenas as ações possiveis, baseadas no mapa
        for a in self.actions:
            position = initial_position + a
            # Verifica se a posição está disponível e se está dentro dos limites do mapa
            if (0 <= position[0] < self.room.shape[0]) and (0 <= position[1] < self.room.shape[1]) and \
                    room[position[0]][position[1]] == 0:
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
        # Vai ter várias posições e caminhos
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


class AgentDFS:
    """
        Busca em profundidade
    """

    def __init__(self, env):
        self.belief_state = env.initial_percepts()
        self.environment = env

    def act(self):
        """
        Faz a ação - algoritmo de busca
        """
        # Começa com uma fronteira com o estado inicial, guarda as posições
        # Vai ter várias posições e caminhos
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
                    # Poda de ciclos - verifica se p já está em path
                    makes_cycle = False
                    # if all(item in path for item in np.array[p[0], p[1]]):
                    for pos in path:
                        if (pos == p).all():
                            makes_cycle = True
                            break
                    if not makes_cycle:
                        # Busca em profuncidade - adiciona no inicio da pilha
                        f = [path + [p]] + f


if __name__ == '__main__':
    room = [[0, 0, 1],
           [1, 0, 1],
           [1, 0, 0]]

    env = Environment([0, 0], [2, 2], room)

    ag = AgentDFS(env)
    path = ag.act()
    print(path)

