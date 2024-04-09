phonebook = {}

entry = input()
while '-' in entry:
    tokens = entry.split('-')
    name = tokens[0]
    phone = tokens[1]
    phonebook[name] = phone

    entry = input()

number_of_searches = int(entry)

for _ in range(number_of_searches):
    name = input()
    if name not in phonebook.keys():
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {phonebook[name]}")

