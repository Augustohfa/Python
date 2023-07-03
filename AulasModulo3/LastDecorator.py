# Ordem dos decoradores

def decorator_parameters(name):
    def decorator(func):
        print(f'Decorator: {name}')

        def new_func(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {name}'
            return final
        return new_func
    return decorator


# A ordem que os decoradores são aplicados é de baixo pra cima
@decorator_parameters(name='Fifth')
@decorator_parameters(name='Fourth')
@decorator_parameters(name='Third')
@decorator_parameters(name='Second')
@decorator_parameters(name='First')
def sum(x, y):
    return x + y


ten_plus_five = sum(10, 5)
print(ten_plus_five)
