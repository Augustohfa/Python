# documentação python -  imutáveis que já vimos: str, int, float, bool

string = 'Augusto Azevedo'
# String não é um objeto mutável exemplo:

# string[3] = 'ABC'  # vai retornar erro pois nao posso alterar parte da string
# Pra fazer isso na str teria que criar uma nova variável
outra_variável = (f'{string[:3]}ABC{string[4:]}')
print(outra_variável)
