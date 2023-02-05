#Operadires lógicos
# and (e) or (ou) not (nao)
# 0 0.0 '' = False
#None que é utilizado pra representar um não valor


# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '1234'

# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Você está entrando')

# elif entrada == 'S':
#     print('Você está saindo')

#  Avaliação de curto circuito - Para de checar no primeiro False
True and True and False and True and True and True
print(bool(0))  #False 
print(bool(0.0))  #False
print(bool(None))  #False
print(bool(False))  #False
print(bool(True))  #True
print(bool(''))  #False
