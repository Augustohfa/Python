import sys
# # sourcery skip: identity-comprehension
# iterable = ['I', 'Have', '__iter__']
# iterator = iter(iterable)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# # Generator expression, Iterables and Iterators em Python

# generator = [num for num in range(1, 11)]
# print(generator)
# print(sys.getsizeof(generator))  # Ocupa muito menos espaço
# for n in generator:
#     print(n)

# Introduction to Generator Function in Python


def generator(n=0):
    yield 1  # Não acaba a função igual o return
    # Mas retorna um valor pausando a função
    print('Continuing...')
    yield 2
    return 'Acabou'


gen = generator(n=0)
print(next(gen))
print(next(gen))


def generator_1(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n > maximum:
            return 'Acabou'


gen_1 = generator_1()

for iterable in gen_1:
    print(iterable)
