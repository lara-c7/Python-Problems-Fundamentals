import re

pattern = r'%([A-Z][a-z]+)%[^\|\$\%\.]*?<(\w+)>[^\|\$\%\.]*?\|(\d+)[^\|\$\%\.]*?\|(\d+\.?\d+?)\$'
total_cost = 0
line = input()
while line != 'end of shift':
    match = re.search(pattern, line)
    if match:
        customer, product, count, price = match.groups()
        total_cost += int(count) * float(price)
        print(f"{customer}: {product} - {int(count) * float(price):.2f}")
    line = input()
print(f"Total income: {total_cost:.2f}")
