class Animal:
    # nome = 'Lion'
    def __init__(self, nome):
        self.nome = nome

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'

    def executar(self, *args, **kwargs):
        ...
# print(nome)  # não vai funcionar pois a classe
#               não está instânciada


# O certo seria
leao = Animal(nome='Leão')
print(leao.nome)
print(leao.comendo('Carne'))
