def criar_mutiplicador(multiplicador):
    def multuplicar(numero):
        return numero * multiplicador
    return multuplicar


duplicar = criar_mutiplicador(2)
triplicar = criar_mutiplicador(3)
quaduplicar = criar_mutiplicador(4)
quintuplicar = criar_mutiplicador(5)

print(duplicar(2))
print(quaduplicar(2))
