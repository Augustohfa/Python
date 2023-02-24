import random
import sys

for i in range(100):
    cpf_gerado = ''
    for i in range(9):
        cpf_gerado += str(random.randint(0, 9))

    primero_caractere = cpf_gerado[0]
    cpf_e_sequencia = cpf_gerado == primero_caractere * len(cpf_gerado)
    if cpf_e_sequencia:
        sys.exit()  # checa se todos os numeros são iguais

    contador = 10
    numeros_multiplicados = []

    for numero in cpf_gerado:
        if contador > 1:
            multiplicador_cpf = int(numero) * contador
            numeros_multiplicados.append(multiplicador_cpf)
            contador -= 1
        else:
            break

    soma_numero = 0

    for numero in numeros_multiplicados:
        soma_numero += numero
    primeiro_numero = (soma_numero * 10) % 11

    digito_1 = primeiro_numero if primeiro_numero <= 9 else 0
    cpf_gerado += str(digito_1)

    # Segundo Digito

    contador_2 = 11
    numeros_multiplicados_2 = []

    for numero_2 in cpf_gerado:
        if contador_2 > 1:
            multiplicador_cpf_2 = int(numero_2) * contador_2
            numeros_multiplicados_2.append(multiplicador_cpf_2)
            contador_2 -= 1
        else:
            break

    soma_numero_2 = 0

    for numero_2 in numeros_multiplicados_2:
        soma_numero_2 += numero_2
    segundo_numero = (soma_numero_2 * 10) % 11

    digito_2 = segundo_numero if segundo_numero <= 9 else 0
    cpf_gerado += str(digito_2)
    print(cpf_gerado, end='\t ')
