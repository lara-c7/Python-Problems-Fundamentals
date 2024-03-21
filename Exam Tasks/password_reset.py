def take_odd(name):
    new_name = ''
    for i in range(len(name)):
        if i % 2 != 0:
            new_name += name[i]
    name = new_name
    return name


def cut(name, idx, lent):
    substr = name[idx:idx + lent]
    name = name.replace(substr, '', 1)
    return name


def sub(name, substr, subst):
    name = name.replace(substr, subst)
    return name


password = input()
command = input()

while command != 'Done':
    tokens = command.split()
    action = tokens[0]
    if action == 'TakeOdd':
        password = take_odd(password)
    elif action == 'Cut':
        index = int(tokens[1])
        length = int(tokens[2])
        password = cut(password, index, length)
    elif action == 'Substitute':
        substring = tokens[1]
        substitute = tokens[2]
        if substring in password:
            password = sub(password, substring, substitute)
        else:
            print("Nothing to replace!")
            command = input()
            continue
    print(password)
    command = input()

print(f"Your password is: {password}")

