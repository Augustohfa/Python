

def factory_decorator(a=None, b=None, c=None):
    def factory_functions(func):
        print('Decorator 1')

        def aninhada(*args, **kwargs):
            print(f'Decorator parameters {a, b, c}')
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return factory_functions
# 'Fábrica de funções' - factory functions


# a partir daqui ele executa a função 'factory_decorator' - vai executar a função
@factory_decorator(1, 2, 3)
def sum(x, y):
    return x + y


decorator = factory_decorator()
# Function definition

multiplica = factory_decorator()(lambda x, y: x * y)
# Criando uma função que multiplica com lambda usando a decoradora


ten_times_five = multiplica(10, 5)
print(ten_times_five)

ten_plus_five = sum(10, 5)
print(ten_plus_five)
