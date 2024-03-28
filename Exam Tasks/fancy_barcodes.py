import re

n = int(input())

pattern = r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'

for _ in range(n):
    line = input()
    # yay, we get to use fullmatch!
    match = re.fullmatch(pattern, line)
    if match:
        barcode = match.group()
        digits = re.findall(r'\d', barcode)
        product_group = ''.join(digits) if digits else '00'
        print(f'Product group: {product_group}')
    else:
        print("Invalid barcode")
