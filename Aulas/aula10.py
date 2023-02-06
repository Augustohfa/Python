# if / elif ......../ else
# se / se não  se / se não

entrada = input('Voce quer entrar ou sair? ')
x = 1

while(x == 1):
    if entrada == 'Entrar': 
        print('Você entrou no sistema!')
        x = x + 1
    elif entrada == 'Sair': 
        print('Voce saiu do sistema!')
        x = x + 1
    else:
        print('Digite "Entrar" ou "Sair"')
        entrada = input('Voce quer entrar ou sair? ')



