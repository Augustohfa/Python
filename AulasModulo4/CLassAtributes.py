ANO_ATUAL = 2023


class Pessoa:
    ano_atual = 2023
    atributo = 'Valor'

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
        # Usar nome_da_classe.atributo para que não modifique seu valor por alguma ventura


p1 = Pessoa('Augusto',21)
p2 = Pessoa('Gabriella', 19)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

# __dict__ e vars para atributos de instâncias
p1.nome = 'Qualquer coisa'
print(p1.__dict__) # Cria um dicionário com os dados do objeto
# Consegue-se também alterar dados com o __dict__
p1.__dict__['nome'] = 'Sla'

# Vars tambem mostra como um dicionário os valores do objeto
print(vars(p1))

# Del deleta uma key do objeto

del p1.__dict__['nome']