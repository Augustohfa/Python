'''
Interando string com while
'''
#       01234567891011
# Objetivo do exercicio, adicionar um * a cada letra do nome

nome = 'Augusto Azevedo'  # Interaveis
tamanho_nome = len(nome)
contador = 0
nova_string = ''

while contador < len(nome):
    nova_string = nova_string + nome[contador] + '*'
    contador += 1

print(nova_string)
