characters = input().split(", ")

char_dict = {ch:ord(ch) for ch in characters}

print(char_dict)