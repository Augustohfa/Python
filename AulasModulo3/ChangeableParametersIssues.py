def adiciona_clientes(nome, lista=[]):
    lista.append(nome)
    return lista


list_1 = []

adiciona_clientes('Augusto', list_1)
adiciona_clientes('Gabriella', list_1)

list_2 = []

adiciona_clientes('Adrielly', list_2)
adiciona_clientes('Yuri', list_2)

clientes2 = adiciona_clientes('Maikon Kuster')
adiciona_clientes('Ken', clientes2)

print(clientes2)
print(list_1)
print(list_2)
print(type(clientes2))