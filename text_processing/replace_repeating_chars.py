char_list = list(input())
final_list = []

i=0
current_char = ""

while True:
    if i == len(char_list):
        break

    if char_list[i] != current_char:
        current_char = char_list[i]
        final_list.append(char_list[i])
    elif char_list[i] == current_char:
        pass

    i += 1

print("".join(final_list))
