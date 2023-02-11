# Calculadora com while
while True:
    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro número: ")
    operador = input("Digite o operador (+ - / *): ")

    try:
        num_1 = float(numero_1)
        num_2 = float(numero_2)
    except ValueError:
        print("Digite apenas números validos")
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print("Operador inválido")
        continue

    if operador == '+':
        print(f'{num_1} + {num_2} é igula a: ', num_1 + num_2)
    elif operador == '-':
        print(f'{num_1} - {num_2} é igula a: ', num_1 - num_2)
    elif operador == '*':
        print(f'{num_1} * {num_2} é igula a: ', num_1 * num_2)
    elif operador == '/':
        print(f'{num_1} / {num_2} é igula a: ', num_1 / num_2)

    sair = input('Quer sair? [S]').upper().startswith('S')

    if sair:
        break
