import re
import sys
initial_text = input()

expression = r"([*\|:]{2})(?P<emoji>[A-Z][a-z]{2,})\1"

emojis = re.finditer(expression, initial_text)
list_of_emojis = []

for bunch in emojis:
    # list_of_emojis.append(bunch.group("emoji"))
    list_of_emojis.append(bunch.group())
# print(list_of_emojis)

#//.|.\\
number_list = []
for char in initial_text:
    if char.isdigit():
        number_list.append(int(char))

cool_treshold = number_list[0]
if len(number_list) > 1:
    for i in range(1,len(number_list)):
        cool_treshold *= number_list[i]
        if cool_treshold >= sys.maxsize:
            cool_treshold = sys.maxsize
            break

#separator
cool_emojis_list = []

for element in list_of_emojis:
    stripped_element = "".join(kk for kk in element if kk.isalpha())
    current_sum = 0
    for ch in stripped_element:
        current_sum += ord(ch)
    if current_sum > cool_treshold:
        cool_emojis_list.append(element)


print(f"Cool threshold: {cool_treshold}")
print(f"{len(list_of_emojis)} emojis found in the text. The cool ones are:")
for cool_emj in cool_emojis_list:
    print(cool_emj)