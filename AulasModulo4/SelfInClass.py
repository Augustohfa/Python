# Entendendo self em classes Python
# Self é uma convenção, poderia ser qualquer
# Qualquer outra coisa, self serve para
# Referênciar a propria instancia
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.

# Quando é chamado o self
# É isso aqui que o Python faz por trás

class Car:
    def __init__(self, name, motor):
        self.name = name
        self.motor = motor

    def acelerar(self):
        print(f'{self.name} está acelerando!')
        print(f'{self.motor} está acelerando!')


# Car.acelerar() não funciona pois vc está
# chamando o molde e não o objeto já criado

mustang = Car('Mustang', 'coyote')

Car.acelerar(mustang)  # Isso aqui é o que acontece
#                       Quando é passado o self no
#                       mustang.acelerar()

mustang.acelerar()  # aqui está sendo passado o self
