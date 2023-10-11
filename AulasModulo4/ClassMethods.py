class Pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def class_method(cls, nome):
        return cls(nome, 50)


pessoa_1 = Pessoa('Augusto', 21)
pessoa_2 = Pessoa.class_method('Augusto')

# Se precisar de um self = é um método de instância


class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password


c1 = Connection()
c1.set_user('Augusto Azevedo')
print(c1.user)
