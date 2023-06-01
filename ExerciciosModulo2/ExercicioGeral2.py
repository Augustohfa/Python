# Adiando execução de funções

def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, arg1):
    def intern(arg2):
        return funcao(arg1, arg2)
    return intern


soma_com_cinco = criar_funcao(soma, 5)

multiplica_por_10 = criar_funcao(multiplica, 10)
print(soma_com_cinco(9))
print(multiplica_por_10(9))
