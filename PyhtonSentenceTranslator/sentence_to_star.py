user_input = input('Digite a frase que você quer traduzir: ')
output = []
user_input_index = 0

for i in user_input:
    if i != ' ':
        output.append('*')
    else:
        output.append(' ')
        user_input_index += 1

str_output = ''.join(output)

print(str_output)
