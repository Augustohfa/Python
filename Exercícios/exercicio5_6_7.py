"""
Faça um programa que peça ao usuário um número inteiro,
informe se este número é par ou impar. Caso o usuário não
digite um número inteiro, informe que não é um número
"""
num_str = (input('Digite um número inteiro: '))
try:
    num = int(num_str)
    if num % 2 == 0:
        print(f'O número {num} é par')
    else:
        print(f'O número {num} é impar')
except ValueError:
    print('Não é um número inteiro.')
"""
Exercício 2
Faça um programa que pergunte a hora ao usuário e, baseando-se
no horário descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12- 17 e Boa noite 18-23
"""
hora = int(input('Digite a hora: '))
if hora >= 0 and hora <= 11:
    print('Bom dia')
elif hora >= 12 and hora <= 17:
    print('Boa tarde')
elif hora >= 18 and hora <= 23:
    print('Boa noite')
"""
Exercício 3
Faça um programa que peça o primeiro nome do usuário. Se o nome
tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6
 letras, escreva "Seu nome é de tamanho normal"; maior que 6 escreva
 "Seu nome é muito grande".s
"""
nome = input('Digite seu nome: ')
if len(nome) >= 4 and len(nome) <= 6:
    print('Seu nome é curto')
elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome é de tamanho normal')
else:
    print('Seu nome é muito grande')
