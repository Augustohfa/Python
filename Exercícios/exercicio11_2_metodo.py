# alternativa para o exercicio 11
lista_de_compras = {
    'Arroz',
    'Salada',
    'Chocolate',
    'Coca cola'
}
while True:
    print('Atualmente sua lista é: ', end='')

    for indice, item in enumerate(lista_de_compras):
        print(f'\n{indice+1}: {item}', end='')

    print('\n', '-' * 20)

    escolha_usuario = input(
        'Deseja adicionar ou remover algum item?: [A]dicionar , '
        '[R]emover,'
        '[S} para fechar o programa,\n'
        '[L] para mostrar a lista novamente: ')

    if escolha_usuario.upper() == 'A':
        produto_adicionar_if = input(
            'Qual item deseja adicionar? '
        )
        lista_de_compras.add(produto_adicionar_if)
        continue

    elif escolha_usuario.upper() == 'R':

        try:
            item_remover = int(input(
                'Qual número do item  que deseja remover? '
            ))
        except ValueError:
            print('Digite um número válido')
        if item_remover > len(lista_de_compras):
            print('Digite um número válido')
        for indice, produto in enumerate(lista_de_compras):
            if indice + 1 == item_remover:
                lista_de_compras.remove(produto)
                break

    elif escolha_usuario.upper() == 'S':
        print('Voce saiu do programa!')
        break
    elif escolha_usuario.upper() == 'L':
        continue
    else:
        print('Comando não válido! ')
        continue
