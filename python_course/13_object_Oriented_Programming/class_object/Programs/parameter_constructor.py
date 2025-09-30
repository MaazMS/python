class Product:

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

p1 = Product("Mi", "mobile", 20000 )
print(p1.name)
print(p1.description)
print(p1.price)
