import re
cpf = input('Digite um CPF: ') \
    .replace(' ', '') \
    .replace('-', '') \
    .replace('.', '')  # replace troca o primeiro caracter pelo 2
cpf = re.sub(
    r'[^0-9]',
    '',
    cpf
)  # tudo que não for um número ele vai substituir por nada

nove_digitos = cpf[:9]

contador_regressivo = 10

resultado = 0
for digito in nove_digitos:
    resultado += int(digito) * contador_regressivo
    contador_regressivo -= 1
digito_1 = (resultado * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
cpf = cpf + str(digito_1)
print(digito_1)

contador_regressivo = 10
dez_digitos = cpf[:10]
resultado = 0
for digito in dez_digitos:
    resultado += int(digito) * contador_regressivo
    contador_regressivo -= 1
digito_2 = (resultado * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
cpf = cpf + str(digito_2)
print(digito_2)

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf == cpf_gerado_pelo_calculo:
    print(f'{cpf} é válido')
else:
    print('CPF inválido')
