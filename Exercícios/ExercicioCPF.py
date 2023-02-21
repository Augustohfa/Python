"""
CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

ex: 746.824.890-70(74682489070)
10   9    8   7    6   5  4   3   2
7    4    6   8    2   4  8   9   0

Somar todos os resultados:
"""
cpf_usuario = input('Digite seu cpf: ')
cpf_errado = False
# remove os caracteres não números do cpf
while True:
    cpf_usuario_so_nmr = ''
    for letra in cpf_usuario:
        if letra == '.' or letra == ' ' or letra == '-':
            continue
        else:
            cpf_usuario_so_nmr += letra
# checa se o tamanho do cpf é 9
    while True:
        if len(cpf_usuario_so_nmr) != 11:
            cpf_usuario = input('Digite um cpf válido: ')
            cpf_errado = True
            break
        else:
            cpf_errado = False
            break
    if cpf_errado:
        continue
    else:
        break


print(len(cpf_usuario_so_nmr))
