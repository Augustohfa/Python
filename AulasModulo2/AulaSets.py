# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno

# Criando um set
# set(iterável) ou {1, 2, 3} ou {} - Cria um deicionário


s1 = set('Augusto')  # Set vazio
print(s1, type(s1))  # Vai iterar o valor iterável

s2 = {'Augusto', 1, 2}  # Set com dados
print(s2)

# Sets são eficientes para remover valores duplicados
# de iteráveis
# - Eles não tem indexes;
# - Eles não garantem ordem;
# - Eles são iteráveis (for, in, not in, etc)

set_1 = {1, 2, 3, 3, 3, 3, 3, 3, 3, 1}
print(set_1)  # remove os valores duplicaods

l1 = [1, 2, 3, 3, 3, 3, 3, 3, 3, 1]
set_1 = set(l1)
l2 = list(set_1)
print(l2)
print(3 in set_1)  # posso iterar sobre o set

# Métodos úteis:
# add. update, clear, discard

s1 = set()
s1.add('Augusto')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4))  # Colocado em tupla para ele iterar
#                                       sobre a tupla e não sobre a string
print(s1)
# s1.clear()  # Limpa o set
s1.discard('Olá mundo')
print(s1)

# Operadores úteis;
# união | união (union) - une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

set_2 = {1, 2, 3}
set_3 = {2, 3, 4}

set_4 = set_2 | set_3
print(set_4)  # União deles retorna 1, 2, 3, 4

set_4 = set_2 & set_3  # Valor que está presente nos dois
print(set_4)

set_4 = set_2 - set_3  # Valor somente no primeiro set
print(set_4)

set_4 = set_3 - set_2  # valor somente no segundo set
print(set_4)

set_4 = set_2 ^ set_3  # Valores que não estão nos dois mutualmente
print(set_4)
