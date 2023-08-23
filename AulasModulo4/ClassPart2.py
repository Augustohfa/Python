class Animal:
    # nome = 'Lion'
    def __init__(self, nome):
        self.nome = nome

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'

    def executar(self, *args, **kwargs):
        ...
# print(nome)  # não vai funcionar pois a classe
#               não está instânciada


# O certo seria
leao = Animal(nome='Leão')
print(leao.nome)
print(leao.comendo('Carne'))

#Mantendo estados dentro da classe


class Cam:
    def __init__(self, name, recording=False):
        self.name = name
        self.recording = recording

    def record(self):
        if self.recording:
            print(f'{self.name} is already recording...')
            return
        print(f'{self.name} has began to record...')
        self.recording = True

        if not self.recording:
            print(f'{self.name} is not recording...')
            return
        print(f'{self.name} has stopped the recording...')
        self.recording = False


cam_1 = Cam('Iphone 13 Pro Max')
cam_2 = Cam('Logitech c920')

cam_1.record()
cam_1.record()

cam_2.record()
cam_2.record()

cam_1.stopRecording()
cam_1.stopRecording()

cam_2.stopRecording()
cam_2.stopRecording()
