contador = 0

while contador < 100:
    contador += 1

    if contador == 6:
        print('O 6 será pulado')
        continue  # Essa expressão faz o laço voltar para o começo, não vai
# ------------------executar nada abaixo dele, voltando direto pro começo do
# ------------------próximo loop
    if contador > 27 and contador < 30:
        print(f'O número {contador} foi eliminado')
        continue

    print(contador)

    if contador == 40:
        break
