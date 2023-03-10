"""
Exercícios
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro.
"""


def executar(funcao, *args):
    return funcao(*args)


def duplicar(numero):
    return numero * 2


def triplicar(numero):
    return numero * 3


def quadriplicar(numero):
    return numero * 4


v = executar(quadriplicar, 12)
print(v)
