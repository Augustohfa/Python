product = {
    'name': 'Caneta Azul',
    'price': 2.5,
    'category': 'office'
}

dc = {
    key: value
    for key, value
    in product.items()
    if key == 'name'
}

print(dc)
