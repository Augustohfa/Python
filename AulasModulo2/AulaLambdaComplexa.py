def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


print(
    executa(
        lambda x, y: x + y,
        2, 3
    )
)

"""
Aqui o lambda funciona como se fosse o 'def'
O primeiro x, y funciona como parametro,
o segundo funciona como o 'return'
mesmo não precisando utulizar return
e o 2, 3 dão os valores pra x e y como se
colocasse no () da funcao ex: funcao(2, 3)
Resumindo esse função lambda acima funciona igual
a
def semNome(x,y):
    return x + y
semNome(2, 3)

por;em com uma linha
"""

# Mesma coisa de:
print(
    executa(soma, 2, 3),
)

# e também:
print(
    soma(2, 3)
)

duplica = cria_multiplicador(2)  # Exemplo pra utilizar função

# Exemplo Lambda:
duplica = executa(
    lambda multiplicador: lambda numero: numero * multiplicador,
    2
)

# Esse exemplo fiz sem assistir o professor mostrar fazendo
# Queria ver se eu conseguiria fazer e fiz certinho 😁
# Como o professor fez:
"""
duplica = executa(
    lambdam m: lambda n: n * m,
    2
)
Basicamente a mesma coisa porém com nome de variáveis diferentes
"""

print(duplica(8))
