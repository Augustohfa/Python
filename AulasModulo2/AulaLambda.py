# Função lambda em Python
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contem apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.

# lista = [4, 31, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)
# print(lista)

listas = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


def ordena(item):
    return item['nome']


l1 = sorted(listas, key=lambda item: item['nome'])
l2 = sorted(listas, key=lambda item: item['sobrenome'])
# lista.sort(key=lambda item: item['nome'])
# key sendo um "método" de sort para ordenar um parâmetro


def exibir_nomes(lista):
    for pessoa in lista:
        print(pessoa.get('nome'), end=' ')
        print(pessoa.get('sobrenome'))


exibir_nomes(l1)
exibir_nomes(l2)
