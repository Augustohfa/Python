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

caminho_arquivo = 'C:\\Users\\AzevedoDev\\Documents\\Udemy\\Python\\udemy_env\\Python\\AulasModulo3\\'
caminho_arquivo += 'CreatingArchives.txt'

# Modo: 'w' apaga tudo que ta no arquivo e escreve de novo nele

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    
    arquivo.writelines(
        
        ('Linha 3\n','Linha 4\n')
    )

print('*' * 40)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())
  

with open(caminho_arquivo, 'a') as arquivo:
    # basicamente um append pra arquivos
    arquivo.write('Fração')
    # testeando utf-8

