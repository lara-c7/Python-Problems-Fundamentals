def take_odd(name):
    one_time = ''
    for i in range(len(name)):
        if i % 2 != 0:
            one_time += name[i]
    name = one_time
    return name


def cut(name, idx, lth):
    name = name[:idx] + name[idx + lth:]
    return name


def sub(name, substr, subst):
    if substr in name:
        name = name.replace(substr, subst)
        return name
    else:
        return 'Nothing to replace!'


password = input()
new_password = ''

while True:
    command = input()
    if command == 'Done':
        break
    tokens = command.split()
    action = tokens[0]
    if action == 'TakeOdd':
        password = take_odd(password)
        print(password)
    elif action == 'Cut':
        index = int(tokens[1])
        length = int(tokens[2])
        password = cut(password, index, length)
        print(password)
    else:
        substring = tokens[1]
        substitute = tokens[2]
        new_password = sub(password, substring, substitute)
        if new_password != 'Nothing to replace!':
            password = new_password
            print(password)
        else:
            print(new_password)

print(f"Your password is: {password}")
