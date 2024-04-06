import re


def decrypt_message(encrypted_message):
    decrypted_message = ''
    letters_count = sum(1 for letter in encrypted_message if letter.lower() in ['s', 't', 'a', 'r'])
    for symbol in encrypted_message:
        decrypted_message += chr(ord(symbol) - letters_count)
    return decrypted_message


def validate_message(msg):
    pattern = r'[^@\-!\:>]*@([A-Za-z]+)[^@\-!\:>]*:(\d+)[^@\-!\:>]*!([AD])![^@\-!\:>]*->(\d+)[^@\-!\:>]*'
    match_re = re.search(pattern, msg)
    return match_re


def process_planets(messages):
    attacked_planets = []
    destroyed_planets = []

    for encrypted_message in messages:
        decrypted_message = decrypt_message(encrypted_message)
        match = validate_message(decrypted_message)
        if match:
            planet_name, _, attack_type, _ = match.groups()
            if attack_type == 'A':
                attacked_planets.append(planet_name)
            elif attack_type == 'D':
                destroyed_planets.append(planet_name)

    return attacked_planets, destroyed_planets


def print_results(attacked_planets, destroyed_planets):
    print(f'Attacked planets: {len(attacked_planets)}')
    for attacked_planet in sorted(attacked_planets):
        print(f'-> {attacked_planet}')
    print(f'Destroyed planets: {len(destroyed_planets)}')
    for destroyed_planet in sorted(destroyed_planets):
        print(f'-> {destroyed_planet}')


if __name__ == "__main__":
    messages_number = int(input())
    messages = [input() for _ in range(messages_number)]

    attacked_planets, destroyed_planets = process_planets(messages)
    print_results(attacked_planets, destroyed_planets)
