import re

n_lines = int(input())
name_pattern = r'\@(\w+)\|'
age_pattern = r'\#(\d+)\*'

for _ in range(n_lines):
    sentence = input()
    name_found = re.findall(name_pattern, sentence)
    age_found = re.findall(age_pattern, sentence)
    print(f"{''.join(name_found)} is {''.join(age_found)} years old.")
