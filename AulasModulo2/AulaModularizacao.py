#  Entendendo meus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a paste onde o __main__ está e as pastas abaixo dele
# Ele não reconhece pastas e modulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos sys.path
# import sys

from AulaModularizacao_m import variable_module, divide


print(__name__)

# print(*sys.path, sep='\n')

print(f'my name is {variable_module}!')

print(divide(8, 2))
