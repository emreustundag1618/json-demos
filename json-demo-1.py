def addProduct(name,price,onsale,category):
    product = {
        "name": name,
        "price": price,
        "onsale": onsale,
        "category": category
    }

    import json
    with open("products.json","w") as file:
        json.dump(product, file, ensure_ascii=False, indent=True)

addProduct("iphone 12",8000,True,["phone","electronics"])

def getProducts():
    import json
    with open("products.json") as file:
        product = json.load(file)

    categories = ' '.join([category for category in product["category"]])
    print(categories)
    print(f'Product name: {product["name"]} price: {product["price"]} categories: {categories}')

getProducts()

