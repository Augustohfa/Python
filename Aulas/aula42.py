"""
enumerate - enumera iteráveis (indices)
"""
lista = ['Augusto', 'Luiz', 'Nicoly']
lista.append('João')
print(lista)

# lista_enumerada = enumerate(lista)
# print(lista_enumerada)  # Pode chamar um next ou for com a lista e a
# transforma em uma tupla enumerada
# for item in lista_enumerada:  # quando é utilizada ele consome o valor, como
# se fosse um push()
#     print(item)

# for item in lista_enumerada:
#     print(item)
for indice, nome in enumerate(lista):
    print(indice, nome)

"""
o que está acontecendo é que, quando você usa o
enumerate na lista, cada indice da lista vira uma tupla
com valores iteraveis númerados, ou seja 'separados'
Ex: (Augusto, Henrique, Ferreira, Azevedo) vai virar
{(0, Augusto), (1, Henrique), (2, Ferreira), (3, Azevedo)}
"""
