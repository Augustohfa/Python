# Mapeamento de dados em List comprehension

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

# It's a list comprehension. It's a way to create a new list from an existing
# list, using just the paramether "price"
# products_price = [
#     product['price'] * 1.05
#     for product in products
# ]

# It's a list comprehension. It's a way to create a new list from an existing
# list, using just the paramether "name"
# products_name = [
#     name['name']
#     for name in products
# ]

# print(*products_price, sep='\n')
# print(*products_name, sep='\n')

# new_products = [
#     {'name': product['name'], 'price': product['price']}
#     for product in products
# ]

# print(*new_products, sep='\n')

# new_products = [
#     {**product, 'price': product['price'] * 1.05}
#     for product in products
# ]

# print(*new_products, sep='\n')

new_products = [
    {**product, 'price': product['price'] * 1.05}
    if product['price'] > 20 else {**product}
    for product in products
]

print(*new_products, sep='\n')


# !Nota: não entendi muito bem ainda como funciona por dentro
# !Com esses for e if, else dentro da list comprehension
# !amanhã dar mais uma pesquisada sobre isso.