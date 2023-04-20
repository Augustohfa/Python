new_list = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'name': 'Augusto'},
]

for item in new_list:
    if isinstance(item, int):
        itemInsideIf = item = item + 5
        print(itemInsideIf)

for item in new_list:
    if isinstance(item, str):
        print(item.upper())
