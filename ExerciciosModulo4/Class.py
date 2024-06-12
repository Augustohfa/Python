'''
Exercício com classes
1 - crie uma classe carro(nome)
2 - crie uma classe motor (nome)
3 - crie uma classe fabricante (nome)
4 - faça a ligação entre Carro e Fabricante
Exiba o nome do carro, motor e fabricante na tela
'''

# Classes


class Car:
    def __init__(self, name, motor, marca):
        self.name = name
        self.motor = motor
        self.marca = marca

    def print_car(self):
        print(
            f'Marca: {self.marca}\n'
            f'Motor: {self.motor}\n'
            f'Modelo: {self.name}\n'
        )


class Engine:
    def __init__(self, engine):
        self.engine = engine


class Manufacturer:
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

# Funções


# def print_class(objeto):
#     print(
#         f'Carro - {objeto.car}'
#     )


bmw = Manufacturer('bmw'.upper())
n46 = Engine('n46')
bmw320i = Car(motor=n46.engine, marca=bmw.manufacturer, name='320i')
bmw320i.print_car()
