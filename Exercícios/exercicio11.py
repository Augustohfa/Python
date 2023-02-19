"""
Fazer um programa que recebe uma lista de compra
O usuário pode apagar, inserir e listar valores
Caso usuário digite um indice inexistente não
deve crashar o programa
"""
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
        'Deseja adicionar ou remover algum item?: [A] para adicionar, '
        '[R] para remover,'
        '[S} para fechar o programa,\n'
        '[L] para mostrar a lista novamente: ')
    if escolha_usuario.upper() == 'A':
        produto_adicionar_if = input(
            'Qual item deseja adicionar? '
        )
        lista_de_compras.add(produto_adicionar_if)
        continue

    elif escolha_usuario.upper() == 'R':
        item_remover = input('Qual item deseja remover? ')

        if item_remover not in lista_de_compras:
            print('Esse item não está na lista de compras!!')
            continue

        lista_de_compras.remove(item_remover)

    elif escolha_usuario.upper() == 'S':
        print('Voce saiu do programa!')
        break
    elif escolha_usuario.upper() == 'L':
        continue
    else:
        print('Comando não válido! ')
        continue
