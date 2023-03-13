# Médoto Get de Dict

p1 = {
    'nome': 'Augusto',
    'sobrenome': 'Azevedo',
    'idade': 20,
}

# Método Get obtém uma chave
# Pode se colocar um valor padrão caso a chave não exista
print(p1.get('nome', "Não existe"))
print(p1['nome'])

# Método pop Apaga um item com a chave informada
# Porém pode adicionar esse item a alguma variável
# Ou utilizalo
nome = p1.pop('nome')

print(nome)

# Popitem faz a mesma coisa do pop porém
# com o último item do dicionário
ultima_chave = p1.popitem()
print(ultima_chave)
print(p1)  # Vai mostrar somente o sobrenome

# Método update pode atualizar um dicionário com outro

p1.update({
    'Nome': 'Augusto',
    'Idade': 21
})
print(p1)
# Outra maneira de fazer o update

tupla = (('Nome', 'Tupla'), ('Idade', 22))
p1.update(tupla)
print(p1)

lista = [['Nome', 'Lista'], ['Idade:', 23]]
p1.update(lista)
print(p1)
