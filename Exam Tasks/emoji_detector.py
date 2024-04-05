from functools import reduce
import re


def the_cool_emotes(emojis):
    cool_emotes = []
    for emote in emojis:
        cool = 0
        for symbol in emote:
            if symbol.isalpha():
                cool += ord(symbol)
        if cool > coolness_threshold:
            cool_emotes.append(emote)
    return cool_emotes


text = input()
pattern = r'\*\*[A-Z][a-z]{2,}\*\*|\:\:[A-Z][a-z]{2,}\:\:'

emote_matches = re.findall(pattern, text)
digits = list(map(int, re.findall(r'\d', text)))
coolness_threshold = reduce(lambda a, b: a * b, digits)

print(f"Cool threshold: {coolness_threshold}")
print(f'{len(emote_matches)} emojis found in the text. The cool ones are:')
the_cool_emotes = the_cool_emotes(emote_matches)
print(*the_cool_emotes, sep='\n')
