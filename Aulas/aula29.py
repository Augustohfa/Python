frase = input('Digite a frase que você quer saber qual'
              'letra aparece mais letras: ')

# Indice
i = 0
# Variables
qtd_apareceu_fora = 0
letra_apareu_mais_vezes = ''
# while function
while i < len(frase):
    letra_atual = frase[i]
    if letra_atual == ' ':
        i += 1
        continue
    qtd_apareceu_dentro = frase.count(letra_atual)

    if qtd_apareceu_fora <= qtd_apareceu_dentro:
        qtd_apareceu_fora = qtd_apareceu_dentro
        letra_apareu_mais_vezes = letra_atual
    i += 1

# User return
print(f'A letra que apareceu mais vezes foi:"{letra_apareu_mais_vezes}"'
      f' aparecendo um total de {qtd_apareceu_fora} vezes')
