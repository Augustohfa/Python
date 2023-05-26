from data_package import products
# Exercícios
# Aumente os preços dos produtos a seguir em 10%



# Ordene os produtos por nome decrescente
# Gere products_ordered_by_name

products_with_new_prices = [
    {**product, 'price': round(product['price'] * 1.1, 2)}
    for product in products
]

products_orded_by_name = sorted(
    products,
    key=lambda product: product['name']
)

print(*products, sep='\n')
print()
print(*products_with_new_prices, sep='\n')
print()
print(*products_orded_by_name, sep='\n')
# Ordene os produtos por preço crescente
# Gere products_ordered_by_price

products_orded_by_price = sorted(
    products_with_new_prices,
    key=lambda product: product['price']

)
print()
print(*products_orded_by_price, sep='\n')
