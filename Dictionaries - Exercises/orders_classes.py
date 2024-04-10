class Product:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def update_price(self, price):
        if self.price != price:
            self.price = price

    def update_quantity(self, quantity):
        self.quantity += quantity


orders = {}

products = input()
while products != 'buy':
    product, price, quantity = products.split()
    if product not in orders.keys():
        orders[product] = Product(float(price), int(quantity))
    else:
        orders[product].update_price(float(price))
        orders[product].update_quantity(int(quantity))

    products = input()

for product, data in orders.items():
    total_price = data.price * data.quantity
    print(f"{product} -> {total_price:.2f}")
