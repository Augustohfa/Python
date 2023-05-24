# from sys import path

# # import pacote_aula  # Importando pacote - porém ele não faz nada

# from pacote_aula.modulo import divide_module as divide  # Agora sim
# # Módulo do pacote

# # Outra forma também seria importar dessa forma
# #  from pacote_aula import modulo

# print(*path, sep='\n')  # Desempacotando a lista de paths do main

# print(divide(8, 2))  # Usando o módulo importado do pacote
from pacote_aula.modulo_oi import fala_oi

print(__name__)
fala_oi()
