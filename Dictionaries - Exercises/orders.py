orders = {}

products = input()
while products != 'buy':
    product, price, quantity = products.split()
    if product not in orders.keys():
        orders[product] = {'price': float(price), 'quantity': int(quantity)}
    else:
        new_quantity = orders[product]['quantity'] + int(quantity)
        orders[product] = {'price': float(price), 'quantity': new_quantity}
    products = input()

for product, data in orders.items():
    print(f"{product} -> {data['price'] * data['quantity']:.2f}")
