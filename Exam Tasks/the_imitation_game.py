message = input()

instruction = input()

while instruction != 'Decode':
    tokens = instruction.split('|')
    action = tokens[0]
    if action == 'Move':
        number_letters = int(tokens[1])
        message = message[number_letters:] + message[:number_letters]
    elif action == 'Insert':
        index = int(tokens[1])
        value = tokens[2]
        message = message[:index] + value + message[index:]
    else:
        substring = tokens[1]
        replace = tokens[2]
        message = message.replace(substring, replace)
    instruction = input()
  
print(f"The decrypted message is: {message}")
