import re

pattern = r'[\@\#]+([a-z]{3,})[\@\#]+[^A-Za-z0-9]*[\/]+(\d+)[\/]+'
text = input()

matches = re.finditer(pattern, text)
for match in matches:
    color, quantity = match.groups()
    print(f"You found {quantity} {color} eggs!")
