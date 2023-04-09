import pprint

# Criar novas listas com filtros


def prettyPrint(v):
    pprint.pprint(v, sort_dicts=False, width=40)


# Print bonito
products = [
    {
        'name': 'Name_1',
        'price': 10,
    },
    {
        'name': 'Name_2',
        'price': 20,
    },
    {
        'name': 'Name_3',
        'price': 30,
    },
]

# Filtro que vem depois do for

prettyPrint(products)

# new_list = list(range(10))

# prettyPrint(new_list)

# filtered_list = []

# for num in new_list:
# if num < 5:
# filtered_list.append(num)

# prettyPrint(filtered_list)

filtered_list_with_comprehension = [num for num in range(10) if num < 5]

prettyPrint(filtered_list_with_comprehension)

new_products = [
    {**products, 'price' : products['price'] * 1.05}
    if products['price'] > 20 else {**products}
    for product in products
    if product['price'] > 10
]
