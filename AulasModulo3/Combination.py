# Combination - Ordem não importa - iterável
# + tamnho grupo
from itertools import combinations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['algodao', 'poliester']
]

combination = list(combinations(pessoas, 2))  # Iterável

print(combination)

print_iter(combination)

print_iter(product(*camisetas))
