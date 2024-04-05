def city_targets():
    targeted_cities = {}
    command = input()
    while command != 'Sail':
        city, pop, gold = command.split('||')
        if city not in targeted_cities.keys():
            targeted_cities[city] = {'population': int(pop), 'gold': int(gold)}
        else:
            targeted_cities[city]['population'] += int(pop)
            targeted_cities[city]['gold'] += int(gold)
        command = input()
    return targeted_cities


def events(targeted_cities):
    while True:
        event = input()
        if event == 'End':
            break
        tokens = event.split('=>')
        action = tokens[0]
        town = tokens[1]
        if action == 'Plunder':
            people = int(tokens[2])
            gold = int(tokens[3])
            targeted_cities[town]['population'] -= people
            targeted_cities[town]['gold'] -= gold
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            if targeted_cities[town]['population'] == 0 or targeted_cities[town]['gold'] == 0:
                del targeted_cities[town]
                print(f"{town} has been wiped off the map!")
        else:
            gold = int(tokens[2])
            if gold < 0:
                print("Gold added cannot be a negative number!")
                continue
            targeted_cities[town]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {targeted_cities[town]['gold']} gold.")
    return targeted_cities


def print_final(targeted_cities):
    if targeted_cities:
        print(f"Ahoy, Captain! There are {len(targeted_cities)} wealthy settlements to go to:")
        for city, city_data in targeted_cities.items():
            print(f"{city} -> Population: {city_data['population']} citizens, Gold: {city_data['gold']} kg")
    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")


if __name__ == '__main__':
    targets = city_targets()
    targeted_towns_left = events(targets)
    print_final(targeted_towns_left)
