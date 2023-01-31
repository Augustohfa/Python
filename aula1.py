# \n - live feed quebra de linha 
# \r \n - -> CRLF
# end= padrao '\n' - quebra de linha após fim do código
print(12, 34, sep='-', end= '\n') 
print(56, 78, sep='-')
#Python = Linguagem de programação 
#Tipo de dipagem = Dinâmica/Forte
#str -> string -> texto
print(1234) #Tipagem dinamica python já detecta que é um número inteiro

#Aspas simples
print('Augusto "Azevedo"') # apenas por estar dentro de aspas ele já identifica que é uma string

#Aspas duplas
print("Augusto 'Azevedo'") # quando quiser usar uma aspas dentro do texto usar aspas diferente da que usou pra abrir srt

#Escape
print("Augusto \"Azevedo\"") # ou também pode ser feito o uso do caracter de escape
#r
print(r"Augusto \"Azevedo\"") # Mostrar inclusive os caracteres de escape - colocar r no começo

print("Augusto 'Azevedo'") # mas continua a melhor maneira usar aspas simples e duplas pra mostrar as aspas 