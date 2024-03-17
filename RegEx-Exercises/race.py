import re

list_of_participants = input().split(', ')
name_pattern = r'[A-Za-z]'
digit_pattern = r'\d'
drivers_info = {}

info = input()
while info != "end of race":
    letters_match = re.findall(name_pattern, info)
    name = ''.join(letters_match)
    if name in list_of_participants:
        digits = [int(digit) for digit in re.findall(digit_pattern, info)]
        distance = sum(digits)
        if name not in drivers_info.keys():
            drivers_info[name] = distance
        else:
            drivers_info[name] += distance
    info = input()
sorted_dict = dict(sorted(drivers_info.items(), key=lambda item: item[1], reverse=True))
counter = 0
sorted_list = []
for key in sorted_dict.keys():
    counter += 1
    sorted_list.append(key)
    if counter == 3:
        break
print(f'1st place: {sorted_list[0]}')
print(f'2nd place: {sorted_list[1]}')
print(f'3rd place: {sorted_list[2]}')
