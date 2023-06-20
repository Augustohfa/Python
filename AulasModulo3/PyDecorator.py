# Decoradores no python são
# "syntax_sugar"

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Decorando função!')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora a função foi decorada!')
        return resultado
    return interna


@criar_funcao  # Passa a função abaixo pra função mencionada no @
# Este é o sysntax_sugar
def inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('Parametro deve ser uma string')


invertida = inverte_string('123')
print(invertida)
