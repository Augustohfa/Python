'''
Exercício - Unir listas
Crie uma função zipper
O trabalho dessa função será unir duas
listas na ordem.
Use todos os valores da menor lista
Ex..:
["Salvador", "Ubatuba", "Belo Horizonte"]

# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
'''

unified_list = []


def zipper(list1, list2):
    min_length = min(len(list1), len(list2))
    for i in range(min_length):
        unified_list.append(list1[i] + '-' + list2[i])
        # Pode-se ser feito com list comprehension - porém odeio
    return unified_list


# Example usage
list1 = ["Salvador", "Ubatuba", "Belo Horizonte"]
list2 = ["BA", "SP", "MG", "RJ"]
unified = zipper(list1, list2)
print(unified)
