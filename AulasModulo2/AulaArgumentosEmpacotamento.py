"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# Lembre do desempacotamento

# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


def soma(*args):
    total = 0
    for numero in args:
        # print(numero)
        total += numero
        # print("Total", total)
    return total

# # soma(1, 2, 3, 4, 5, 6)


# soma_1_2_3 = soma(1, 2, 3)
# print(soma_1_2_3)

# soma_4_5_6 = soma(4, 5, 6)
# print(soma_4_5_6)

# numeros = (1, 2, 3, 4, 5, 6)

# print(sum((1, 2, 3, 4, 5, 6)))

numeros = 1, 2, 3, 4, 5

outra_soma = soma(*numeros)
print(outra_soma)
print(numeros)
print(*numeros)

# empacotamento e desempacotamento
