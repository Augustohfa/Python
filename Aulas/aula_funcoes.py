#Tambem vindo do ChatGPT o conhecimento de Funções, estou estudando por fora do curso com o mesmo.

def str_to_int(str):
    str = int(str)


def is_int(number):
    return isinstance(number), int

numero = input('Digite um número: ')    
str_to_int(numero)

if (is_int):
    print(numero)

else:
    print('Não é um número')


#Código da erro logo no começo se eu o usuário digitar algo que não é um número porém isso seria
#Facilmente resolvido colocando um int(input() na variável numero e fazendo um if para determinar que só contiue o 
#codigo se o que foi digitado pelo usuário fosse um numero inteiro


