"""
split e join com list e str
split - divide uma string
join - une uma sring
"""
frase = 'Olha só que, coisa interessante'
# lista_palavras = frase.split()  # coloca cada palavra como um objeto em lista
lista_frase_crua = frase.split(',')


lista_frases = []
for i, frase in enumerate(lista_frase_crua):
    # strip corta os espaços lstrip e rstrip (esquerda e direita)
    # lista_frases[i] = lista_frase_crua[i].strip
    lista_frases.append(lista_frase_crua[i].strip())

# print(lista_frases)
# print(lista_frase_crua)

frases_unidas = ','.join(lista_frases)
print(frases_unidas)
