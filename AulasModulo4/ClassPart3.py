class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando')

        print(f'{self.nome} está filmando...')
        self.filmando = True

    def parar_filmagem(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando!')

        print(f'{self.nome} está parando de filmar!')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode tirar foto enquanto filma!')
            return

        print(f'{self.nome} está fotografando.')


c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()

print(c1.filmando)
print(c2.filmando)
