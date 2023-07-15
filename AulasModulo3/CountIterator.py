# Count é um iterador sem fim
# Muito similar ao range - porém não acaba
from itertools import count

c1 = count()
r1 = range(100)

print(next(c1))
print(next(c1))
print(next(c1))

print('c1', hasattr(c1, '__iter__'))
print('r1', hasattr(r1, '__iter__'))

print('Count')

for i in c1:
    if i > 100:
        break
    print(i)

print()

for i in r1:
    if i > 100:
        break
    print(i)
