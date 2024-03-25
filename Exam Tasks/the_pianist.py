number_of_pieces = int(input())
musical_pieces = {}

for _ in range(number_of_pieces):
    piece, composer, key = input().split('|')
    musical_pieces[piece] = {'composer': composer, 'key': key}

command = input()
while command != 'Stop':
    tokens = command.split('|')
    action = tokens[0]
    piece = tokens[1]
    
    if action == 'Add':
        composer = tokens[2]
        key = tokens[3]
        if piece not in musical_pieces.keys():
            musical_pieces[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif action == 'Remove':
        if piece in musical_pieces.keys():
            musical_pieces.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif action == 'ChangeKey':
        new_key = tokens[2]
        if piece in musical_pieces.keys():
            musical_pieces[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    
command = input()

for piece, info in musical_pieces.items():
    print(f"{piece} -> Composer: {info['composer']}, Key: {info['key']}")
