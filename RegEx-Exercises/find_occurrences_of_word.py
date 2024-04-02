import re

sentence = input()


pattern = fr'(?i)\b{word_to_search}\b'
matches = re.findall(pattern, sentence)

print(len(matches))
