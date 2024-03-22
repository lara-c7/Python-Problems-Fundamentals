import re

line = input()

pattern = r'(?i)([#\|])([a-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'

matches = re.finditer(pattern, line)
total_calories = 0

data = []
for match in matches:
    total_calories += int(match.group(4))
    data.append(f'Item: {match.group(2)}, Best before: {match.group(3)}, Nutrition: {match.group(4)}')
print(f'You have food to last you for: {total_calories // 2000} days!')
print('\n'.join(data))
