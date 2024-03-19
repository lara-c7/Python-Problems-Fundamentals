import re

sentence = input()
word_to_search = input()

pattern = fr'(?i)\b{word_to_search}\b'
matches = re.findall(pattern, sentence)

print(len(matches))
