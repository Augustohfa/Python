# # for
# texto = 'Python'

# i = 0
# tamanho_string = len(texto)

# while i < tamanho_string:
#     print(texto[i])

#     i += 1
# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_digitada != senha_salva:
#     if repeticoes != 0:
#         print('Senha incorreta!')
#     senha_digitada = (input('Digite uma senha: '))
#     repeticoes += 1

# print(
#     f'A senha foi digitada errada'
#     f' {repeticoes} vezes.')
# Esse laço podem ter infinitas repetições
texto = 'Python'
novo_texto = ''

# Para cada letra em texto exiba letra na tela
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto)
