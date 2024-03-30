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
for plant, plant_data in plants_dict.items():
    average_rating = float(sum(plant_data['rating']) / len(plant_data['rating'])) if len(plant_data['rating']) > 0 \
        else 0
    print(f"- {plant}; Rarity: {plant_data['rarity']}; Rating: {average_rating:.2f}")

