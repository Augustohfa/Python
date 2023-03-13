import copy
# copy  - retona uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especifica(del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

d2 = d1.copy()

d2['c1'] = 1000
d2['l1'][1] = 99999
# Shallow Copy ou traduzindo copia raza não
# entra nos subniveis
# Para que copie também os subníveis e eles parem de apontar
# pro mesmo endereço de memória que a "original" dele
# tem que fazer um deepcopy, que é um método do copy
# mas pra isso temos que importar o "copy"

# ex

d3 = copy.deepcopy(d1)
# Agora d3 é = a d1 porém se você alterar d3 não irá alterar d1

print(d2)
print(d1)
# como d2 = d1 aponta o Dicionário D1 para o endereço de memória
# de D1, alterar um, acaba alterando o outro também
# por isso temos o método copy.

d2['c1'] = 1000
print(d1)
print(d2)
