# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower)

    if 'l' in letras:
        print('Parabéns você achou a letra misteriósa!')
        break

    print(letras)
