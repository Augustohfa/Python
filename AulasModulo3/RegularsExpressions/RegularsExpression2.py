import re

userMessage = input(
    'Whats is your office, and house number? (DDD)XXXXX-XXXX \n')
# phoneNumberRegex = re.compile('\(\\d\\d\)\\d\\d\\d\\d\\d\-\\d\\d\\d\\d')
# print(f'The phone numbers found are: {messageSearch.group()}')

# Pode-se agrupar os conjuntos de números,
# por exemplo o DDD, utilizando '(' ')'.

phoneNumberRegexWithDDD = re.compile(
    '(\(\\d\\d\\))(\\d\\d\\d\\d\\d\-\\d\\d\\d\\d)')
messageSearch = phoneNumberRegexWithDDD.search(userMessage)

# Ainda pode dar print no número todo
print(f'The phone numbers found are: {messageSearch.group()}')

# Pra receber somentne o DDD:
print(f'Area Code: {messageSearch.group(1)}')
print(f'Main number: {messageSearch.group(2)}')

# Ou pode adicionar os conjuntos em varáveis
# com o método "groups()"

areaCode, mainNumber = messageSearch.groups()
print(f'Area code: {areaCode}')
print(f'Main number: {mainNumber}')


# Revisão da correspondência com expressão regular
# Embora haja diversos passos para usar expressões regulares em Python, cada passo é bem simples.
# 1. Importe o módulo de regex usando import re.
# 2. Crie um objeto Regex usando a função re.compile(). (Lembre-se de usar uma string pura.)
# 3. Passe a string que você quer pesquisar ao método search() do objeto Regex. Isso fará um objeto Match ser retornado.
# 4. Chame o método group() do objeto Match para retornar uma string com o texto correspondente.
