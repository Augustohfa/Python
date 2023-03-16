# Sistemas de perguntas e respostas
import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2? ',
        'opcoes': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5x5? ',
        'opcoes': ['25', '20', '50', '15'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quunto é 10/2? ',
        'opcoes': ['3', '5', '4', '4'],
        'Resposta': '5'
    },
]

respostas_certas = 0
respostas_erradas = 0

for pergunta in perguntas:
    numero_opcao = 0

    print(f'Pergunta: {pergunta.get("Pergunta")}', end='\n\n')
    print('Opções: ')

    for opcoes in pergunta.get('opcoes'):
        numero_opcao += 1
        print(f'{numero_opcao}) {opcoes}')

    resposta_usuario = input('Digite sua resposta: ')

    os.system('clear')

    if resposta_usuario == pergunta.get('Resposta'):
        print('Você acertou!', end='\n \n')
        respostas_certas += 1

    else:
        print('Resposta errada!')
        respostas_erradas += 1

if respostas_certas == 1:
    print(f'Você acertou {respostas_certas} resposta')
else:
    print(f'Você acertou {respostas_certas} respostas')

print(f'Você errou {respostas_erradas} respostas')
