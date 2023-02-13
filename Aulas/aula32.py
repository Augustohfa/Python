"""
Iterável - > str, range, etc
Iterador - > quem sabe entregar um valor por vez
next - > me entrega o próximo valor
iter - > me entregue seu iterador
"""
# texto = iter('Augusto')  # __iter__() "entregador"
# # texto.metodo
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())  # chama o próximo valor


# for letra in texto   como funciona por baixo dos panos
########################################################################
texto = 'Augusto'  # iterável
iterador = iter(texto)  # iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
# For faz exatamente isso "por baixo dos panos"
########################################################################
for letra in texto:
    print(letra)
# Exatamente isso
