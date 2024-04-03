def lower_upper(user, data):
    user = user.lower() if data[1] == 'Lower' else user.upper()
    return user


def reverse(user, starter, end):
    substring = user[starter:end + 1]
    substring = substring[::-1]
    return substring


def substring_func(user, substr):
    if substr in user:
        user = user.replace(substr, '')
        return user
    else:
        return f"The username {user} doesn't contain {substr}."


def start():
    username = input()
    command = input()

    while command != 'Registration':
        tokens = command.split()
        action = tokens[0]

        if action == 'Letters':
            username = lower_upper(username, tokens)
            print(username)

        elif action == 'Reverse':
            start_index = int(tokens[1])
            end_index = int(tokens[2])
            if 0 <= start_index < len(username) and 0 <= end_index < len(username):
                print(reverse(username, start_index, end_index))

        elif action == 'Substring':
            substring = tokens[1]
            username = substring_func(username, substring)
            print(username)

        elif action == 'Replace':
            char = tokens[1]
            username = username.replace(char, '-')
            print(username)

        else:
            char = tokens[1]
            if char in username:
                print('Valid username.')
            else:
                print(f"{char} must be contained in your username.")

        command = input()


start()
