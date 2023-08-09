'''
Criando arquivos com Python
Usamos a função open para abrir
um arquivo em Python (ele pode ou não existir)
Modos:
r (read), w (write), x (create
a (escreve no final), b (binário),
t (modo texto), + (leitura e escrita)

Context manager - with (abre e fecha)
Métodos Uteis
write, read (escrever e ler)
writelines (escrever várias linhas)
seek (move o cursor)
readline (ler linha)
readlines (ler linhas)

Sobre o Módulo OS:

os.remove ou unlink - apaga arquivo
os.rename = troca o nome do arquivo

Módulo JSON:
json.dump - gera um arquivo JSON
json.load
'''

import os
import json


caminho_arquivo = 'C:\\Users\\AzevedoDev\\Documents\\Udemy\\Python\\udemy_env\\Python\\AulasModulo3\\'
caminho_arquivo += 'CreatingArchives.json'

# Modo: 'w' apaga tudo que ta no arquivo e escreve de novo nele

# with open(caminho_arquivo, 'w+') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
    
#     arquivo.writelines(
        
#         ('Linha 3\n','Linha 4\n')
#     )

# print('*' * 40)

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())
  

# with open(caminho_arquivo, 'a') as arquivo:
#     # basicamente um append pra arquivos
#     arquivo.write('Fração')
#     # testeando utf-8

pessoa = {
    'name' : 'Augusto',
    'last_name' : 'Azevedo',
    
    'enderecos' : [
        {'rua' : 'Rua Sei la das quantas', 'número' : 38},
        {'rua' : 'Rua dois sei la o que', 'número' : 48}
    ],
    
    'favorite_colors' : (
        'Purple', 'Black',
    ),
    
    'heigh' : 1.89,
    'dev' : True,
    'diabetic' : True
}


with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    json.dump(pessoa,
              arquivo,
              ensure_ascii=False,
              indent=2,
              )

with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
    pessoa_1 = json.load(arquivo)

name_pessoa_1 = pessoa_1.get('name',) + ' ' + pessoa_1.get('last_name')
print(name_pessoa_1)