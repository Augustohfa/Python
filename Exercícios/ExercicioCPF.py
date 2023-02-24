import sys
cpf_usuario = input('Digite seu cpf: ')
cpf_usuario_so_nmr = ''
# remove os caracteres não números do cpf

primero_caractere = cpf_usuario[0]
cpf_e_sequencia = cpf_usuario == primero_caractere * len(cpf_usuario)
if cpf_e_sequencia:
    sys.exit()  # checa se todos os numeros são iguais


def tirar_tracos_cpf(cpf):
    cpf_usuario_so_nmr = ''
    for letra in cpf:
        if letra == '.' or letra == ' ' or letra == '-':
            continue
        else:
            cpf_usuario_so_nmr += letra
    return cpf_usuario_so_nmr


# checa se o tamanho do cpf é 9
while True:
    try:
        cpf_sem_traços = tirar_tracos_cpf(cpf_usuario)
        cpf_numero_int = int(cpf_sem_traços)
        break
    except ValueError:
        cpf_usuario = input('Digite um CPF válido: ')


while True:
    if len(cpf_sem_traços) != 11:
        cpf_usuario = input('Digite um CPF válido: ')
        tirar_tracos_cpf(cpf_usuario)
        continue
    else:
        break

contador = 10
numeros_multiplicados = []

for numero in cpf_sem_traços:
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

# Segundo Digito

contador_2 = 11
numeros_multiplicados_2 = []

for numero_2 in cpf_sem_traços:
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


print(cpf_usuario)
print(numeros_multiplicados_2)
print(digito_1)
print(digito_2)
