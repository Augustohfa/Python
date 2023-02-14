"""
Faça um jogo para o usuário adivinhar qual a
palavra secreta
    - Você vai propor uma palavra secreta qualquer
e vai dar a possibilidade para o usuário
digitar apenas uma letra.
    - Quando o usuário digitar uma letra, você
vai conferir se a letra digitada uma letra,
você vai conferir se a ;etra digitada está
na palavra secreta.
    - Se a letra digitada estiver na palavra
    secreta; exiba *.
Faça a contagem de tentativas do seu usuário
"""

# Váriaveis
palavra_secreta = 'palavra'
tentativas = 0
letras_certas = ''
# Entrada
while True:
    letra_digitada = input('Digite uma letra: ')
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra: ')
        continue
    tentativas += 1

    if letra_digitada in palavra_secreta:
        letras_certas += letra_digitada
    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in letras_certas:
            palavra_formada += letra
        else:
            palavra_formada += '*'
    print(palavra_formada)
    if palavra_formada == palavra_secreta:
        print(f'Você acertou em {tentativas} tentativas!')
        break
# Esse foi bem complicadinho de pensar em tudo, tive q
# debugar algumas vezes pra entender porque as palavras
# não estavam se formando e as vezes não aparecendo
# mas no fim deu tudo certo, consegui fazer
# sem a solução do professor
