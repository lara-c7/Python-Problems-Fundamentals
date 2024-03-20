import re

line = input()
pattern = r'#[A-Za-z]{3,}##[A-Za-z]{3,}#|@[A-Za-z]{3,}@@[A-Za-z]{3,}@'
word_pattern = r'[A-Za-z]+'
valid_pairs = re.findall(pattern, line)
mirror_pairs = []

if len(valid_pairs) > 0:
    print(f"{len(valid_pairs)} word pairs found!")
    for pair in valid_pairs:
        words = re.findall(word_pattern, pair)
        if words[0] == words[1][::-1]:
            mirror_pairs.append(f'{words[0]} <=> {words[1]}')
    if mirror_pairs:
        print("The mirror words are: ")
        print(', '.join(mirror_pairs))
    else:
        print("No mirror words!")
else:
    print("No word pairs found!")
    print("No mirror words!")
