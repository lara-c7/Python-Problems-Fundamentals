number_heroes = int(input())
heroes_dict = {}

for _ in range(number_heroes):
    hero, hp, mp = input().split()
    heroes_dict[hero] = {'hp': int(hp), 'mp': int(mp)}

while True:
    command = input()
    if command == 'End':
        break
    tokens = command.split(' - ')
    action = tokens[0]
    hero = tokens[1]
    if action == 'CastSpell':
        mp_needed = int(tokens[2])
        spell_name = tokens[3]
        if heroes_dict[hero]['mp'] >= mp_needed:
            heroes_dict[hero]['mp'] -= mp_needed
            print(f"{hero} has successfully cast {spell_name} and now has {heroes_dict[hero]['mp']} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")
    elif action == 'TakeDamage':
        damage = int(tokens[2])
        attacker = tokens[3]
        heroes_dict[hero]['hp'] -= damage
        if heroes_dict[hero]['hp'] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero]['hp']} HP left!")
        else:
            heroes_dict.pop(hero)
            print(f"{hero} has been killed by {attacker}!")
    elif action == 'Recharge':
        amount = int(tokens[2])
        initial_mp = heroes_dict[hero]['mp']
        heroes_dict[hero]['mp'] += amount
        if heroes_dict[hero]['mp'] > 200:
            heroes_dict[hero]['mp'] = 200
            new_amount = heroes_dict[hero]['mp'] - initial_mp
            print(f"{hero} recharged for {new_amount} MP!")
            continue
        print(f"{hero} recharged for {amount} MP!")
    elif action == 'Heal':
        amount = int(tokens[2])
        initial_hp = heroes_dict[hero]['hp']
        heroes_dict[hero]['hp'] += amount
        if heroes_dict[hero]['hp'] > 100:
            heroes_dict[hero]['hp'] = 100
            new_amount = heroes_dict[hero]['hp'] - initial_hp
            print(f"{hero} healed for {new_amount} HP!")
            continue
        print(f"{hero} healed for {amount} HP!")

for hero, hero_data in heroes_dict.items():
    print(f'{hero}')
    print(f"  HP: {hero_data['hp']}")
    print(f"  MP: {hero_data['mp']}")
