"""
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
Sinal - ou +
Ex: 0>-100, .1f
conversion flags = !r !s !a vamos voltar nesse assunto mais na frente no curso
"""
variavel = 'ABC'

print(f'{variavel:->10}')
print(f'{variavel:-<10}')
print(f'{variavel:-^10}')
print(f'{1000.324242342:+.1f}')

print(f'{variavel:-<10}')
