"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento
"""


def soma(x, y, z=None):
    # Definição
    if z is not None:
        print(f'{x=} +, {y=} + {z=}', '|', 'X + Y + Z = ', x + y + z)
    else:
        print(f'{x=} +, {y=}', '|', 'X + Y = ', x + y)


soma(1, 2, 3)
soma(y=2, z=3, x=1)

# Valores padrõres para paâmetros
# Refatorar = editar código.
soma(1, 2)
soma(3, 5)
soma(100, 200)
