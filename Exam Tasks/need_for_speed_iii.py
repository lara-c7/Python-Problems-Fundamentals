number_of_cars = int(input())
car_dict = {}

for _ in range(number_of_cars):
    car, mileage, fuel = input().split('|')
    car_dict[car] = {'mileage': int(mileage), 'fuel': int(fuel)

while True:
    tokens = input().split(' : ')
    if tokens[0] == 'Stop':
        break
    action = tokens[0]
    car = tokens[1]
    if action == 'Drive':
        distance = int(tokens[2])
        fuel = int(tokens[3])
        if car_dict[car]['fuel'] >= fuel:
            car_dict[car]['mileage'] += distance
            car_dict[car]['fuel'] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if car_dict[car]['mileage'] >= 100000:
                removed_car = car_dict.pop(car)
                print(f"Time to sell the {car}!")
        else:
            print("Not enough fuel to make that ride")
    elif action == 'Refuel':
        fuel = int(tokens[2])
        initial_fuel = car_dict[car]['fuel']
        car_dict[car]['fuel'] += fuel
        if car_dict[car]['fuel'] > 75:
            car_dict[car]['fuel'] = 75
            refueled = 75 - initial_fuel
            print(f"{car} refueled with {refueled} liters")
        else:
            print(f"{car} refueled with {fuel} liters")
    else:
        km = int(tokens[2])
        car_dict[car]['mileage'] -= km
        if car_dict[car]['mileage'] < 10000:
            car_dict[car]['mileage'] = 10000
        else:
            print(f"{car} mileage decreased by {km} kilometers")

for car, car_info in car_dict.items():
    print(f"{car} -> Mileage: {car_info['mileage']} kms, Fuel in the tank: {car_info['fuel']} lt.")
