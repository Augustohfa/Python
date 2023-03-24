# List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.


# print(list(range(1, 11)))

number_list = []
for number in range(1, 10):
    number_list.append(number)

# print(list)

# Creating a list of numbers from 1 to 10.
number_list_2 = [
    numero
    for numero in range(1, 11)
]
print(number_list_2)

# Creating a list of numbers from 1 to 10, and multiplying each number by 2.
number_list_3 = [
    numero * 2
    for numero in range(1, 11)
]
print(number_list_3)
