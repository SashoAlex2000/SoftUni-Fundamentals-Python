#bruuuh
import re
bought_furniture = []
line = input()
total_sum = 0
regex = r"[>]+[A-Za-z]+[<<]+[0-9\.]+[\!][0-9]"

while line != "Purchase":
    command = re.finditer(regex, line)
    for match in command:
        furniture = match.group(1)
        price = match.group(2)
        quantity = match.group(3)
    bought_furniture.append(furniture)
    current_sum = quantity * price
    total_sum += current_sum

print(bought_furniture)
print(total_sum)







