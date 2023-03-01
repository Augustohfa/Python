"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo código é alcaçavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""
x = 'Modulo'


def escopo():
    x = 'Escopo'
    print(x)

    def outra_funcao():
        x = 'Outra função'
        print(x)
    outra_funcao()


escopo()
print(x)
