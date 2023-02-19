"""
Listas de listas e seus indicices
"""
salas = [
    #  0          1
    ['Maria', 'Helena'],  # 0
    # 0
    ['Elanine'],  # 1
    # 0        1        2
    ['Augusto', 'João', 'Eduarda'],  # 2
]
aluno_fora = []
qtd_salas = 0

for numero_sala, alunos_sala in enumerate(salas):
    print(f'Sala: {numero_sala + 1}')
    for nome in alunos_sala:
        print(f'Aluno: {nome}')
