#Operador lógico "not"


senha = input("senha: ")


if  not senha: # isso significa que a partir do momento que  'senha' voltar um valora falso, esse if vai ser rodado, pois o if not ao contrario do if sozinho vai rodar aquele código em que o resultado seja "False"
    #como por exemplo o senha acima, caso o usuário não digite nada, pois a str vazia é considerada um 'Falsy'
    print('Senha incorreta')


print(not False) # true
print(not True) # false
print(not 0) # false
print(not 1) # true
print(not 'teste') # false
print(not'') # false
print(not None) # false # resumindo  o 'not' serve para inverter a expressão