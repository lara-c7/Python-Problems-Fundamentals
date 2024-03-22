import re


def days_enough_food(calories):
    total_days = calories // 2000
    return total_days


def product_data(match_one):
    item = match_one.group(2)
    expire_date = match_one.group(3)
    calories = match_one.group(4)
    return f'Item: {item}, Best before: {expire_date}, Nutrition: {calories}'


line = input()

pattern = r'(?i)([#\|])([a-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'

matches = re.finditer(pattern, line)
total_calories = 0

data = []
for match in matches:
    total_calories += int(match.group(4))
    data.append(product_data(match))
print(f'You have food to last you for: {days_enough_food(total_calories)} days!')
print('\n'.join(data))

