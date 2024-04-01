def add_stop(stops, idx, string):
    if 0 <= idx < len(stops):
        stops = stops[:idx] + string + stops[idx:]
    return stops


def stop_remove(stops, start_idx, end_idx):
    if 0 <= start_idx < len(stops) and 0 <= end_idx < len(stops):
        stops = stops[:start_idx] + stops[end_idx + 1:]
        # string_to_remove = stops[start_idx:end_idx + 1]
        # stops = stops.replace(string_to_remove, '')
    return stops


all_stops = input()

command = input()
while command != 'Travel':
    tokens = command.split(':')
    action = tokens[0]
    if action == 'Add Stop':
        index = int(tokens[1])
        strings = tokens[2]
        all_stops = add_stop(all_stops, index, strings)
    elif action == 'Remove Stop':
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        all_stops = stop_remove(all_stops, start_index, end_index)
    else:
        old_string = tokens[1]
        new_string = tokens[2]
        if old_string in all_stops:
            all_stops = all_stops.replace(old_string, new_string)

    print(all_stops)
    command = input()

print(f"Ready for world tour! Planned stops: {all_stops}")
