# Yield from


def gen1():
    yield 1
    yield 2
    yield 3


def gen2():
    yield from gen1()
    yield 4
    yield 5
    yield 6


def gen3():
    yield 7
    yield 8
    yield 9


g1 = gen2()
g2 = gen3()

for numero in g1:
    print(numero)

for numero in g2:
    print(numero)
