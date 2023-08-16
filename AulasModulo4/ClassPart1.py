class Person:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


# Ao invés de fazer p1.nome e p1.sobrenome
# estamos declarando dentro da init no objeto
# fazendo um molde
p1 = Person('Augusto', 'Azevedo')
# Python cria um objeto e joga esses valores nele
# jogando para seus atributos

# Métodos em instâncias de classes em Python


# Hard coded
# class Carro:
#     def __init__(self):
#         self.nome = 'Lancer Evolution X'
#
#
# lancer_evo_x = Carro()
# print(lancer_evo_x.nome)

# self se referencia ao próprio objeto 'Car'

class Car:
    def __init__(self, modelo):  # todo metodo precisa como primeiro parâmetro
                                 # o 'self' para se referênciar ao objeto
        self.modelo = modelo

    def acelerar(self):
        print(f'{self.modelo} está acelerando!')


lancer_evo_x = Car(
    'Lancer Evolution X'
)
mustang_mach1 = Car(
    'Mach 1'
)
print(mustang_mach1.modelo)
lancer_evo_x.acelerar()
