"""
Cuidados com dados mutáveis
= - copiando o valor (imutaveis)
= - aponta para o mesmo valor na memória(mutáveis)
"""
lista_nomes = ['Luiz', 'Maria']
lista_a = lista_nomes
print(lista_a)

lista_nomes[0] = 'Augusto'
# Mesmo mudando apenas a primeira lista, ela "altera a segunda" também,
# pois quando é mutável o sinal de = aponta pro mesmo valor

# Para copiar e fazer duas listas diferentes existem metodos
