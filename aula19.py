"""
Fautiamento de strings novamente
0123456789
Olá mundo
-987654321
Fatiamento [inicio:fim:parte] [::]
Obs: a função len retorna a qtd de caracteres na string
"""

variavel = 'Olá mundo'
print(
    variavel[4:]  # vai retornar apenas a string após o 4º indice
)
print(
    variavel[:5]  # vai retornar apenas a string anterior ao 5º indice
)
# aqui começo a utilizar novas linhas pra me organizar melhor dentro
# dos códigos (achei melhor pessoalmente)
print(
    len(variavel)  # vai retornar a quantidade/tamanho da string
)
print(
    variavel[0:9:2]
)
# vai retornar os indices de 0 a 9 pulando eles de 2 em 2 ( o último número)
print(
    variavel[-1:-10:-1]
)
# vai retornar a string ao contrário, só que precisa ser tudo invertido, os indices vão do -1 ao
# primeiro indice da string ao contrario.
