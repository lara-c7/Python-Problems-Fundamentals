def fill_book():
    phonebook = {}

    while True:
        entry = input().split('-')

        if len(entry) == 1:
            return phonebook, int(entry[0])

        name, number = entry
        phonebook[name] = number


def search_name(phonebook, name):
    if name in phonebook.keys():
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")


def start():
    phonebook, number = fill_book()

    for _ in range(number):
        name_to_search = input()
        search_name(phonebook, name_to_search)


if __name__ == '__main__':
    start()
