# Métodos úteis dos dicionários em Python
# len  - quantas chaves
# keys - iteráve; com as chaves
# value - iterável com valores
# items - iterável com chaves e valores
# setdefault - adiciona um valor se a chave não existe
# copy  - retona uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especifica(del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Augusto',
    'sobrenome': 'Azevedo',
    # 'idade': 20,
}
pessoa.setdefault('idade', 'Não informado')


print(len(pessoa))
print(list(pessoa.keys()))


print(list(pessoa.values()))

print()

for chave in pessoa.values():
    print(chave)

print()

for chave in pessoa:
    print(chave)

print()

for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')
