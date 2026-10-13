def search_products(products, query):
    query = query.casefold()

    return [
        product
        for product in products
        if query in product.casefold()
    ]


products = ["Python Book", "Django Course", "SQL Guide"]

print(search_products(products, "python"))