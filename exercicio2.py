nome = 'Augusto Azevedo'
altura = 1.88
peso = 75


imc = peso / altura ** 2


#Formatção de str
linha_1 = f'{nome} tem {altura:.2f} de altura pesa {peso} quilos e seu IMC é {imc:.2f}' 

print(linha_1)