import re


def make(ps, token):
    idx = int(token[2])
    if token[1] == 'Upper':
        ps = ps[:idx] + ps[idx].upper() + ps[idx + 1:]
    elif token[1] == 'Lower':
        ps = ps[:idx] + ps[idx].lower() + ps[idx + 1:]
    return ps


def insert(ps, token):
    idx = int(token[1])
    char = token[2]
    ps = ps[:idx] + char + ps[idx:]
    return ps


def replace(ps, token):
    char = token[1]
    value = int(token[2])
    new_char = chr(ord(char) + value)
    ps = ps.replace(char, new_char)
    return ps


def validation(ps):
    pattern = r'[A-Za-z0-9\_]+'
    if len(ps) < 8:
        print("Password must be at least 8 characters long!")
    if not re.match(pattern, ps):
        print("Password must consist only of letters, digits and _!")
    upper = False
    lower = False
    digit = False
    for ch in ps:
        if ch.islower():
            lower = True
        elif ch.isupper():
            upper = True
        elif ch.isdigit():
            digit = True
    if not upper:
        print("Password must consist at least one uppercase letter!")
    if not lower:
        print("Password must consist at least one lowercase letter!")
    if not digit:
        print("Password must consist at least one digit!")


def main():
    password = input()

    command = input()
    while command != 'Complete':
        tokens = command.split()
        if tokens[0] == 'Make':
            password = make(password, tokens)
        elif tokens[0] == 'Insert':
            if 0 <= int(tokens[1]) < len(password):
                password = insert(password, tokens)
        elif tokens[0] == 'Replace':
            if tokens[1] in password:
                password = replace(password, tokens)
        elif tokens[0] == 'Validation':
            validation(password)
            command = input()
            continue
        else:
            command = input()
            continue
        print(password)
        command = input()


if __name__ == '__main__':
    main()
