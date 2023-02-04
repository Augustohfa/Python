primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

#O exercício é comparar os dois valores e retornar pro usuario qual valora é maior, usando if


if primeiro_valor > segundo_valor:
    print(f'O primeiro valor: {primeiro_valor} é maior que o segundo valor: {segundo_valor}')
elif segundo_valor > primeiro_valor:
    print(f'O segundo valor: {segundo_valor} é maior que o primeiro valor: {primeiro_valor}')
elif segundo_valor == primeiro_valor:
    print(f'Os dois valores são iguais')