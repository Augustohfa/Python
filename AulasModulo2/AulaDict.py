"""
Dicionários em Python, tipo dict
Dicionários são estruturas de dados do tipo
Par de "Chave" e "valor",
Chaves podem ser consideradas como o "índice"
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc/
O valor pode ser de qualquer tipo, incluindo outro
dicionário
Usamos as chaves  - {} - ou a classe disct para criar
dicionários
Imutáveis: str, intm floar, bool, tuple
Mutáve: dict, list
pessoa = {
    'nome': 'Augusto'
    'sobrenome': 'Azevedo'
    'idade': 18
    'altura': 1.88
    'endereços': [
        {'rua': 'Rua tal', 'número': 123},
        {'rua': 'Outra rua', 'número': 321},
    ]
}
print(pessoa, type(pessoa))
"""
pessoa = {
    'nome': 'Augusto',
    'sobrenome': 'Azevedo',
    'idade': 18,
    'altura': 1.88,
    'endereços': [
        {'rua': 'Rua tal', 'número': 123},
        {'rua': 'Outra rua', 'número': 321},
    ],
}
# print(pessoa, type(pessoa))

print(pessoa['nome'])
print()
# é basicamente um objeto do JavaScript

for chave in pessoa:
    print(chave)
