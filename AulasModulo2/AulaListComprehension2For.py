import pprint
new_list = []

# for x in range(3):
#     for y in range(3):
#         new_list.append((x, y))

# list_with_comprehension = [
#     x
#     for x in range(3)
# ]

# # print(new_list)
# print(list_with_comprehension)

# list_1 = [
#     [letter for letter in 'Augusto']
# ]
# # print(list_1)

# new_list_adds_2 = [
#     number + 2 for number in list_with_comprehension
# ]

# # new_list_adds_2_ = []
# # for tuple_ in list_with_comprehension:
# #     for number in tuple_:
# #         new_list_adds_2_.append(number)

# pprint.pprint(new_list_adds_2)

new_list = [
    [(x, letra) for letra in 'Augusto']
    for x in range(3)
]

pprint.pprint(new_list)
