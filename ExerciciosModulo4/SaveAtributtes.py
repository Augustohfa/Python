# Exercício - Salve sua Classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados
import json

# Json declaration
file_path = 'saveAtributes.json'


class PersonalComputer:

    def __init__(self, turned_on, name, year, touchbar, processor, ram, screensize):
        self.turned_on = False
        self.name = name
        self.year = year
        self.touchbar = touchbar
        self.processor = processor
        self.ram = ram
        self.screesize = screensize

    def turn_on(self):
        if not self.turned_on:
            self.turned_on = True
        else:
            print(f'{self.name} is already On')


macbook = PersonalComputer(
    False,
    'MacBook Pro',
    2016,
    True,
    'i7',
    16,
    15)


macbook.turn_on()

macbook_dict = {

}

for macbookKeys in macbook.__dict__:
    macbook_dict.update(macbook.__dict__)


with open(file_path, 'w') as json_file:
    json.dump(macbook_dict, json_file, indent=2)


# print(macbook_dict)
with open(file_path, 'r') as json_file:
    macbook_atributtes = json.load(json_file)


print(*macbook_atributtes.values())

macbook_from_json = PersonalComputer(*macbook_atributtes.values())
print(macbook_from_json.name)