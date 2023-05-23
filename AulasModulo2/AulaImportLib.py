import importlib

import AulaModularizacao_m

print(AulaModularizacao_m.divide(8, 2))

for index in range(1, 11):
    print(index)
    # import AulaModularizacao_m  # não vai importar por motivos de - singlelib
    importlib.reload(AulaModularizacao_m)  # Vai recarregar o módulo
