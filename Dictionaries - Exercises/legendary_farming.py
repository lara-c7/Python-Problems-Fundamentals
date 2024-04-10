legends = {'shards': 0, 'fragments': 0, 'motes': 0}
is_obtained = False
legendary_item = ''

materials = input()
while not is_obtained:
    materials_lst = materials.split()
    for i in range(0, len(materials_lst), 2):
        quantity = int(materials_lst[i])
        material = materials_lst[i + 1].lower()
        if material not in legends.keys():
            legends[material] = 0
        legends[material] += quantity
        if legends['shards'] >= 250:
            legendary_item = 'Shadowmourne'
            is_obtained = True
            legends['shards'] -= 250
        elif legends['fragments'] >= 250:
            legendary_item = 'Valanyr'
            is_obtained = True
            legends['fragments'] -= 250
        elif legends['motes'] >= 250:
            legendary_item = 'Dragonwrath'
            is_obtained = True
            legends['motes'] -= 250
        if is_obtained:
            print(f"{legendary_item} obtained!")
            break
    if is_obtained:
        break

    materials = input()

for material, quantity in legends.items():
    print(f"{material}: {quantity}")
