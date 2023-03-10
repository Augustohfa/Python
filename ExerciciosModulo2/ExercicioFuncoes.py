# Exercicio com funções

# Crie uma função que multiplica todos argumentos
# Não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável

# Crie uma função que fala se um número é par ou ímpar
# Retorne se o número é par ou ímpar

def multiplica(*args):
    total = 1
    for numero in args:
        total = total * numero
    return total


print(multiplica(1, 2, 3, 4))


def parOuImpar(numero):
    if numero % 2 == 0:
        resposta = print(f'O {numero} é par!')
    else:
        resposta = print(f'O {numero} é impar!')
    return resposta


numero = input('Digite um número: ')

try:
    numero = int(numero)
    parOuImpar(numero)

except ValueError:
    print('Digite um número inteiro: ')
