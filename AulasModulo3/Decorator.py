import time

# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em oturas funções


def create_func(func):

    # Função decoradora
    def inside(*args, **kwargs):
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)

        return result

    return inside


def inverte_string(string_inserida):
    return string_inserida[::-1]


def is_string(parameter):
    if not isinstance(parameter, str):
        raise TypeError('Parâmetro deve ser uma String')


checking_parameter = create_func(inverte_string)
invertido = checking_parameter('Testing')
print(invertido)


def duration_calc(inside_function):
    def wrapper():

        # Calculate time of execution
        incial_time = time.time()
        inside_function()
        final_time = time.time()
        total_time = final_time - incial_time

        # Shows the formated message on screen

        print(f'{inside_function} Execution time: {total_time}')

    return wrapper


# Create the function that will be decorated
def main():
    for n in range(0, 10):
        pass


# Calls function
wrapper_var = duration_calc(main)
wrapper_var()
