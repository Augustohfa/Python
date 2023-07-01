'''
print('how are you doing?') 
value = 2

if value > 10:
    print('Value is greater than  10')
else:
    print('Value is less than 10')

def somaNumero(x,y):
    return x + y
    
numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Agora digite o segundo número: '))


print(f'A soma entre os dois números é {somaNumero(numero_1,numero_2)}')
'''

class Person:
    name = 'Augusto'
    occupation = 'Software Developer'
    networth = 10
   
a = Person()

print(a.name)
print(Person.occupation)