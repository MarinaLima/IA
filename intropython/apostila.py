"""
    Resolver todos os exerc ́ıcios da apostila de Python, dispon ́ıvel em: 
    http://antigo.scl.ifsp. edu.br/portal/arquivos/2016.05.04_Apostila_Python_-_PET_ADS_S%C3%A3o_Carlos.pdf
"""

# 3.4 Exercícios: strings
"""
  1 – Considere a string A = "Um elefante incomoda muita gente". Que fatia corresponde a "elefante
  incomoda"? A[3:20]
"""


def read_phrase():
    """
        2 - Escreva um programa que solicite uma frase ao usuário e escreva a frase toda em maiúscula e sem espaços
        em branco.
    """
    x = input("Entre com uma frase: ")
    print("Se for pra remover apenas espaços em branco antes e depois da frase:")
    print((x.strip()).upper() + "\n")
    print("Se for pra remover TODOS os espaços em branco da frase:")
    print((x.replace(" ", "")).upper() + "\n\n")


# 4.2 Exercícios: números

def calc_z():
    """
        1 – Escreva um programa que receba 2 valores do tipo inteiro x e y, e calcule o valor de z:
        z = (𝑥2+𝑦^2) / (𝑥−𝑦)2
    """
    x = int(input("Entre com o valor de x: "))
    y = int(input("Entre com o valor de y: "))
    z = (x**2 + y**2) / (x-y)**2
    print(z)

def update_salary():
    """
    2 – Escreva um programa que receba o salário de um funcionário (float), e retorne o resultado do novo salário com
    reajuste de 35%.
    """
    salary = float(input("Entre com o salario: "))
    new_salary =  salary * 1.35
    print(new_salary)


# 5.5 Exercícios: listas

def print_list_infos():
    """
    1 – Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
        a) tamanho da lista.
        b) maior valor da lista.
        c) menor valor da lista.
        d) soma de todos os elementos da lista.
        e) lista em ordem crescente.
        f) lista em ordem decrescente.
    """
    L = [5, 7, 2, 9, 4, 1, 3]
    print("Tamanho da lista: ", len(L))
    print("Maior valor da lista: ", max(L))
    print("Menor valor da lista: ", min(L))
    print("Soma de todos os elementos da lista: ", sum(L))
    # TODO não funciona
    print("Lista em ordem crescente: ", L.sort())
    print("Lista em ordem decrescente: ", L.reverse())


def generate_list():
    """
    2 – Gere uma lista contendo os múltiplos de 3 entre 1 e 50.
    """
    print(list(range(3, 50, 3)))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_phrase()
    calc_z()
    update_salary()
    print_list_infos()
    generate_list()
