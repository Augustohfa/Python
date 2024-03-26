# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação entre dois
# ou mais objetos
# Cada objeto terá seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# Objeto tem um ou muitos objetos
# Os objetos podem viver separadamente, mas pode se tratar
# de uma relação onde um objeto precisa de outro
# para fazer determinada tarefa
# (existem controversias sobre as definições de agregação)

class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum(p.preco for p in self._produtos)

    def adicionar_produtos(self, *produtos):
        self._produtos.extend(produtos)

    def listar_produtos(self):
        for produto in self._produtos:
            print(f'- {produto.nome} R${produto.preco:.2f}')
        print(f'Total: R${carrinho.total():.2f}')


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()

p1, p2 = Produto('Caneta', 1.20), Produto('Lapis', 1.00)

carrinho.adicionar_produtos(p1, p2)

carrinho.listar_produtos()
