def register(name, license_plate, parking_):
    if name in parking_.keys():
        print(f"ERROR: already registered with plate number {parking_[name]}")
    else:
        parking_[name] = license_plate
        print(f"{name} registered {license_plate} successfully")
    return parking_


def unregister(name, parking_):
    if name not in parking_.keys():
        print(f"ERROR: user {name} not found")
    else:
        parking.pop(name)
        print(f"{name} unregistered successfully")
    return parking_


def main_f(number_plates):
    for _ in range(number_plates):
        command = input().split()
        action = command[0]
        username = command[1]
        if action == 'register':
            license_plate = command[2]
            register(username, license_plate, parking)
        else:
            unregister(username, parking)

    for user, license_plate in parking.items():
        print(f"{user} => {license_plate}")


number_of_plates = int(input())
parking = {}
main_f(number_of_plates)
