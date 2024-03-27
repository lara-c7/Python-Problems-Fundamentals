key = [int(el) for el in input().split()]

stringer = input()
while stringer != 'find':
    decrypted = ''
    if len(stringer) > len(key):
        repetitions = len(stringer) // len(key)
        new_key = key * repetitions
        if len(stringer) > len(key):
            difference = len(stringer) - len(key)
            new_key += new_key[:difference]
    else:
        new_key = key
      
    for index, symbol in enumerate(stringer):
        decrypted += chr(ord(symbol) - new_key[index])
      
    treasure = decrypted.split('&')[1]
    coordinates_start = decrypted.index('<')
    coordinates_end = decrypted.index('>')
    coordinates = decrypted[coordinates_start + 1:coordinates_end]
    print(f"Found {treasure} at {coordinates}")
    
    stringer = input()
