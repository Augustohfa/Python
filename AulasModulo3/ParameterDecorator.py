def decorator(func):
    print('Decorator 1')

    def aninhada(*args, **kwargs):
        print('Aninhada')
        res = func(*args, **kwargs)
        return res
    return aninhada


@decorator  # a partir daqui ele executa a função 'decorator'
def sum(x, y):
    return x + y


ten_plus_five = sum(10, 5)

print(ten_plus_five)
