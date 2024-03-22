stock = {}

command = input()
sold_count = 0
while command != 'Complete':
    action, quantity, food = command.split()
    quantity = int(quantity)
    if action == 'Receive':
        if quantity <= 0:
            command = input()
            continue
        if food not in stock.keys():
            stock[food] = 0
        stock[food] += quantity
    else:
        if food not in stock.keys():
            print(f"You do not have any {food}.")
        elif quantity > stock[food]:
            sold_count += stock[food]
            sold_quantity = stock.pop(food)
            print(f"There aren't enough {food}. You sold the last {sold_quantity} of them.")
        else:
            stock[food] -= quantity
            sold_count += quantity
            print(f"You sold {quantity} {food}.")
            if stock[food] == 0:
                del stock[food]

    command = input()

for food, quantity in stock.items():
    print(f"{food}: {quantity}")
print(f"All sold: {sold_count} goods")
