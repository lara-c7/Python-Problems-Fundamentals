# Race
# Write a program that processes information about a race. 
# On the first line, you will be given a list of participants separated by ", ". 
# On the next few lines until you receive a line "end of race"
# you will be given some info which will be some alphanumeric characters.
# In between them, you could have some extra characters which you should ignore.
# For example: "G!32e%o7r#32g$235@!2e". The letters are the name of the person and the sum of the digits is the distance he ran.
# So here we have George who ran 29 km. Store the information about the person only if the list of racers contains the name of the person.
# If you receive the same person more than once just add the distance to his old distance.
# At the end print the top 3 racers ordered by distance in descending in the format:
# "1st place: {first racer}
# 2nd place: {second racer}
# 3rd place: {third racer}"


────────────────────────────────────────


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
