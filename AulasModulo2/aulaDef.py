"""
Introdução às funções (def) em Python
Funções são trexos de código usados para
replicar determinada açao ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None(nada)
"""


def print_4(a, b, c):
    print(a)
    print(b)
    print(c)


def saudacao(nome):
    print(f'Olá, {nome}')


print_4('1', '2', '3')
saudacao('Augusto')
saudacao('Henrique')


def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é multiplo de {multiplo}?', end=' ')
    print(resultado)


multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)
