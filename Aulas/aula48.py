"""
Aula por fora, queria aprender um pouco sobre
funcoes em python, ja que poderia ter sido muito
util no exercicio de cpf
"""


cpf_usuario = input('Digite seu cpf: ')
cpf_errado = False
cpf_usuario_so_nmr = ''
# remove os caracteres não números do cpf


def tirar_tracos_cpf(cpf):
    cpf_usuario_so_nmr = ''
    for letra in cpf:
        if letra == '.' or letra == ' ' or letra == '-':
            continue
        else:
            cpf_usuario_so_nmr += letra
    return cpf_usuario_so_nmr

# checa se o tamanho do cpf é 9


cpf_sem_traços = tirar_tracos_cpf(cpf_usuario)

while True:
    if cpf_sem_traços != 11:
        cpf_usuario = input('Digite um CPF válido: ')
        tirar_tracos_cpf(cpf_usuario)
        continue
    else:
        break
print(cpf_usuario)
