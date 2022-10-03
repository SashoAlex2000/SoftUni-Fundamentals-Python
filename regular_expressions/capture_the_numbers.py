import re

pattern = r'\d+'
number_list = []

while True:
    text = input()
    if not text:
        break

    result = re.findall(pattern,text)

    if len(result):
        number_list.append(" ".join(result))


print(" ".join(number_list))
