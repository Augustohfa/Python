#  Operadores in e not in
#  Strings são interáveis // ou seja, você pode navegar item por item, letra por letra na palavra/string
#  0 1 2 3 4 5 6
#  A u g u s t o
#  -6 -5 -4 -3 -2 -1

# nome = 'Augusto'
# print(nome[2])
# print(nome[-5]) # contado de trás pra frente
# print('g' in nome) # g está entre as letras da str nome?
# print(10 * '-')
# print('g' not in nome) # g não está entre as letras da str nome?

nome = input('Digite seu nome: ')
find = input('Digite o que você quer encontrar: ')

if find in nome:
    print(f' "{find}" está em {nome}')
else:
    print(f'"{find}" não está em {nome}')