# Listas em python
"""
Listas em python
Tipo list - Mutàvel
Suporta varios valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend e +
"""
lista = [
    #    0     1           2            3
    123, True, 'Augusto Azevedo', 1.2, [
        'String dentro da lista dentro da lista'
    ]
]
lista[3] = 'Maria'
print(type(lista[3]))
numero = input('Digite um número: ')
print(lista[int(numero)])
