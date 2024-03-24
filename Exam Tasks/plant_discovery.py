plants_dict = {}
n_lines = int(input())

for _ in range(n_lines):
    plant, rarity = input().split('<->')
    plants_dict[plant] = {'rarity': rarity, 'ratings': []}

command = input()
while command != 'Exhibition':
    first_split = command.split(' - ')
    second_split = first_split[0].split(': ')
    action = second_split[0]
    plant = second_split[1]
    if plant not in plants_dict.keys():
        print('error')
    elif action == 'Rate':
        rating = int(first_split[1])
        plants_dict[plant]['ratings'].append(rating)
    elif action == 'Update':
        new_rarity = first_split[1]
        plants_dict[plant]['rarity'] = new_rarity
    else:
        plants_dict[plant]['ratings'] = []

    command = input()

print("Plants for the exhibition:")
for plant, plant_info in plants_dict.items():
    if plant_info['ratings']:
        print(f"- {plant}; Rarity: {plant_info['rarity']}; Rating: \
{(sum(plant_info['ratings']) / len(plant_info['ratings'])):.2f}")
    else:
        print(f"- {plant}; Rarity: {plant_info['rarity']}; Rating: 0.00")
