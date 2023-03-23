# # Empacotamento e desempacotamento de dicionários

# a, b = 1, 2
# a, b = b, a  # Invertendo valor das variáveis


# person = {
#     'nome': 'Augusto',
#     'sobrenome': 'Azevedo',
#     'nome_2:': 'Nicoly',
#     'sobrenome_2': 'Braz',
# }

# # a, b = person  # Isso vai me retornar 'nome', 'sobrenome'

# # a, b = person.values()  # Agora sim vai me retornar o valor

# # a, b = person.items()  # Vai me retornar tupla com valor e variavel

# # Ou por exemplo usar desempacotamento dentro de desempacotamento

# # Unpacking the items of the dictionary into two tuples.
# (variable_nome_1, name_person_1, *rest) = person.items()
# (variable_name_2, name_person_2) = rest


# print(variable_nome_1, name_person_1, variable_name_2, name_person_2)


# for key, value in person.items():
#     print(key, value)

# data_person = {
#     'age': 20,
#     'high': 1.89,
# }

# complete_person = person | data_person

# print(complete_person)

# # args e kwars
# kwargs - keyword arguments (argumentos nomeados)

person = {
    'name': 'Augusto',
    'second_name': 'Azevedo',
}
person_data = {
    'age': 20,
    'height': 1.89,
}

complete_person = person | person_data


def show_keyword_arguments(*args, **kwargs):
    print('Nao nomeados: ', args)

    for key, value in kwargs.items():
        print(key, '\b: ', value)


show_keyword_arguments(nome='Joana', qlq=123)

show_keyword_arguments(nome='Augusto', idade=20)

show_keyword_arguments(1, 2)

show_keyword_arguments(**complete_person)

configs = {
    'argument_1': 'value_1',
    'argument_2': 'value_2',
    'argument_3': 'value_3',
    'argument_4': 'value_4',
}