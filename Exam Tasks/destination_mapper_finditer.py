import re


def destination_data(data):
    pattern = r'([=\/])([A-Z][A-Za-z]{2,})\1'
    matches = re.finditer(pattern, data)
    travel_points = 0
    destinations = []

    for match in matches:
        destinations.append(match.group(2))
        travel_points += len(match.group(2))
    return f"Destinations: {', '.join(destinations)}\nTravel Points: {travel_points}"


text = input()
print(destination_data(text))
