import re


def regex_validate(msg):
    pattern = r'[^@\-!\:>]*@([A-Za-z]+)[^@\-!\:>]*:(\d+)[^@\-!\:>]*!([AD])![^@\-!\:>]*->(\d+)[^@\-!\:>]*'
    match_re = re.search(pattern, msg)
    if match_re:
        return match_re
    else:
        return False


messages_number = int(input())
attacked_planets = []
destroyed_planets = []

for _ in range(messages_number):
    encrypted_message = input()
    decrypted_message = ''
    letters_count = 0
    for letter in encrypted_message:
        if letter.lower() in ['s', 't', 'a', 'r']:
            letters_count += 1
    for symbol in encrypted_message:
        decrypted_message += chr(ord(symbol) - letters_count)

    match = regex_validate(decrypted_message)
    if match:
        planet_name, population, attack_type, soldier_count = match.groups()
        if attack_type == 'A':
            attacked_planets.append(planet_name)
        elif attack_type == 'D':
            destroyed_planets.append(planet_name)


print(f'Attacked planets: {len(attacked_planets)}')
for attacked_planet in sorted(attacked_planets):
    print(f'-> {attacked_planet}')
print(f'Destroyed planets: {len(destroyed_planets)}')
for destroyed_planet in sorted(destroyed_planets):
    print(f'-> {destroyed_planet}')
