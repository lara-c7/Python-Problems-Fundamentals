first_char = input()
second_char = input()
rand_string = input()
total_sum = 0

for char in rand_string:
    if ord(first_char) < ord(char) < ord(second_char):
        total_sum += ord(char)
print(total_sum)
