import copy as cp


def gac(nodes, consts):
    """
    Graph arc consistency
    :return:
    """
    # para cada restição olha a variável que está no scopo
    to_do = [{'var': v, 'cons': c} for c in consts for v in c['scope']]
    #
    # for t in to_do:
    #     print(t)

    gac2(nodes, consts, to_do)


def gac2(nodes, consts, to_do):
    while to_do:
        arc = to_do.pop(0)
        x = arc['var']
        ys = cp.copy(arc['cons']['scope'])
        ys.remove(x)
        cons = arc['cons']

        new_domain = []
        dx = cp.copy(nodes[x])

        while dx:
            x_val = dx.pop(0)
            for y in ys:
                if x_val in new_domain:
                    break
                for y_val in nodes[y]:
                    # ** em python serve para desempacotar dicionários em variáveis
                    if cons['cons'](**{x: x_val, y: y_val}):
                        new_domain.append(x_val)
                        break

        if new_domain != dx:
            nodes[x] = cp.copy(new_domain)
            for c_prime in consts:
                if c_prime['name'] != cons['name'] and x in c_prime['scope']:
                    for z in c_prime['scope']:
                        if z != x:
                            to_do.append({'var': z, 'cons': c_prime})


if __name__ == "__main__":

    nodes = {'A': [1, 2, 3, 4],
             'B': [1, 2, 3, 4],
             'C': [1, 2, 3, 4]
             }

    # restrições = arcos
    consts = [{'name': 'C1', 'scope': ['A', 'B'], 'cons': lambda A, B: A < B},
              {'name': 'C2', 'scope': ['B', 'C'], 'cons': lambda B, C: B < C}]

    print(consts[0]['cons'](10, 15))

    for n in nodes:
        print('{} : {}'.format(n, nodes[n]))

    gac(nodes, consts)

    for n in nodes:
        print('{} : {}'.format(n, nodes[n]))
