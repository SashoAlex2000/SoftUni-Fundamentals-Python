import re
from math import floor
line = input()

result = re.findall(r"([#|\|])([A-Z][a-zA-Z ]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1", line)

# print(result)
total_available_calories = 0

for shite in result:
    total_available_calories += int(shite[3])

print(f"You have food to last you for: {floor(total_available_calories/2000)} days!")

for shite in result:
    print(f"Item: {shite[1]}, Best before: {shite[2]}, Nutrition: {shite[3]}")