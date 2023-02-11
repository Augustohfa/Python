"""
Repetições
while (enquanto)
Executa uma repetição enquanto uma condição for verdadeira
Loop infinito (quando um código não tem fim)
"""
condicao = True

while condicao:
    nome = input('Qual seu nome: ')
    print(f'Seu nome é {nome}')
    break

    condicao = input('Deseja continuar? [S/N] ').upper()
    if condicao == 'N':
        break
