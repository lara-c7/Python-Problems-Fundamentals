def contain(raw_key, instructions):
    substring = instructions[1]
    if substring in raw_key:
        return f"{raw_key} contains {substring}"
    else:
        return "Substring not found!"


def flip(raw_key, instructions):
    start_index = int(instructions[2])
    end_index = int(instructions[3])
    raw_key_part = raw_key[start_index:end_index].upper() if instructions[1] == 'Upper' \
        else raw_key[start_index:end_index].lower()
    raw_key = raw_key[:start_index] + raw_key_part + raw_key[end_index:]
    return raw_key


def slicer(raw_key, instructions):
    start_index = int(instructions[1])
    end_index = int(instructions[2])
    raw_key = raw_key[:start_index] + raw_key[end_index:]
    return raw_key


raw_activation_key = input()


def activate(raw_key):
    command = input()
    while command != 'Generate':
        instructions = command.split('>>>')
        instruct = instructions[0]
        
        if instruct == 'Contains':
            print(contain(raw_key, instructions))
        elif instruct == 'Flip':
            raw_key = flip(raw_key, instructions)
            print(raw_key)
        elif instruct == 'Slice':
            raw_key = slicer(raw_key, instructions)
            print(raw_key)

        command = input()
    return f"Your activation key is: {raw_key}"


print(activate(raw_activation_key))
