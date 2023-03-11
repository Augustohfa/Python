# Manipulando chaves e valores em dicionários

pessoa = {}


# pessoa['nome'] = 'Augusto'
# print(pessoa['nome'])
chave = 'nome'
pessoa[chave] = 'Augusto'
lista = []

print(pessoa[chave])

pessoa[chave] = 'Nicoly'
print(pessoa[chave])

pessoa['sobrenome'] = 'Braz'
# del pessoa['sobrenome']


# print(pessoa['Sobrenome'])

# Código vai parar por aqui. Por causa da exxceção
if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])
