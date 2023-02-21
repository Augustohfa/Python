string = 'ABCD'
lista = ['Maria', 'Helena', 'Eduarda']
tupla = 'Python', 'é', 'Legal'
salas = [
    ['Maria', 'Helena', 'Eduarda'],
    ['Augusto', 'Ferreira'],
    ['September', 'Ferreira'],
]
# a, b, *_, c = lista  # Vai pegar todo valor entre o segundo e o ultimo.
# print(a, c)


# for nome in lista:
#     print(nome, end=' ', sep='')
print(*lista)  # colocar o * na frente da lista fica igual o for acima
print(*string)
print(*tupla)
print(*salas)
