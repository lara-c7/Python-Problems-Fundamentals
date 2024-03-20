def insert_space(name, idx):
    name = name[:idx] + ' ' + name[idx:]
    return name


def reverse(name, substr):
    name = name.replace(substr, '', 1)
    substr = substr[::-1]
    name += substr
    return name


def change_all(name, substr, replaced):
    name = name.replace(substr, replaced)
    return name


message = input()

command = input()
while command != 'Reveal':
    tokens = command.split(':|:')
    action = tokens[0]
    if action == 'InsertSpace':
        index = int(tokens[1])
        message = insert_space(message, index)
        print(message)
    elif action == 'Reverse':
        substring = tokens[1]
        if substring in message:
            message = reverse(message, substring)
            print(message)
        else:
            print('error')
    elif action == 'ChangeAll':
        substring = tokens[1]
        replacement = tokens[2]
        message = change_all(message, substring, replacement)
        print(message)
    command = input()

print(f"You have a new text message: {message}")
