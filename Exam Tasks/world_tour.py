all_stops = input()

command = input()
while command != 'Travel':
    tokens = command.split(':')
    action = tokens[0]
    if action == 'Add Stop':
        index = int(tokens[1])
        string_one = tokens[2]
        if 0 <= index < len(all_stops):
            all_stops = all_stops[:index] + string_one + all_stops[index:]
    elif action == 'Remove Stop':
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        if 0 <= start_index < len(all_stops) and 0 <= end_index < len(all_stops):
            all_stops = all_stops[:start_index] + all_stops[end_index + 1:]
    else:
        old_string = tokens[1]
        new_string = tokens[2]
        if old_string in all_stops:
            all_stops = all_stops.replace(old_string, new_string)
    print(all_stops)
    command = input()

print(f"Ready for world tour! Planned stops: {all_stops}")
