# @property - um getter no modo 'pythonico'
# getter - um método para obter um atributo
# é um método que se comporta como um
# atributo
# Geralmente é usada nas seguintes situações:
# - como getter
#  p/ evitar quebrar código do cliente
#  p/ habilitar um setter
#  p/ executar ações ao obter um atributo

# Classes #########################

class Caneta:
    def __init__(self, cor):
        self.cor_caneta = cor

    def getCor(self):  # getter, versao pythonica
        # aqui eu posso mudar o nome do atributo quando eu quiser
        # sem alterar o codigo fora da classe
        # mudando apenas dentro do 'getCor()' o self.cor
        print('Get cor está rodando')
        return self.cor_caneta

    def set_cor(self, cor):  # setter modo pythonico
        print('Set cor está rodando')
        self.cor_caneta = cor


# Objetos ##########################################

caneta_1 = Caneta('Azul')


# Code ##############################

print(caneta_1.getCor())

caneta_1.set_cor('Verde')
print(caneta_1.getCor())
