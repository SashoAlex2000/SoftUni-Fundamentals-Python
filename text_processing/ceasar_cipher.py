initial_word = input()

char_list = []

for ch in initial_word:
    char_list.append(chr(ord(ch) + 3))

print("".join(char_list))