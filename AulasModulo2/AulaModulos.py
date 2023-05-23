# Módulos padrão Python (Import, from, as e *)
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes

# import sys

# print(sys.platform)

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes_pequenos
# Desvantagens: Sem o namesapce do módulo


# importa plataform como plataforma, para utilizar linha 29
from sys import platform as plataforma

import sys as sistema  # importa o módulo com outro nome

from sys import platform

print(platform)  # Aqui agora o 'platform' puxa o kernel q voce esta usando
# Não necessita mais colocar 'sys.platform'. Tomar cuidado com isso

# Alias 1 - importe nome_modulo as apelido

print(sistema.platform)

# Alias 2 - from nome_modulo import objeto as apelido


print(plataforma)

# má pratica - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo do módulo
