parking = {}

number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split()
    action = command[0]
    username = command[1]
    if action == 'register':
        license_plate_num = command[2]
        if username in parking.keys():
            print(f"ERROR: already registered with plate number {parking[username]}")
        else:
            parking[username] = license_plate_num
            print(f"{username} registered {license_plate_num} successfully")
    else:
        if username not in parking.keys():
            print(f"ERROR: user {username} not found")
        else:
            parking.pop(username)
            print(f"{username} unregistered successfully")

for user, license_plate in parking.items():
    print(f"{user} => {license_plate}")
