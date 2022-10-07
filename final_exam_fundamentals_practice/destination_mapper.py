import re

total_sum = 0
destinations = input()
expression = r"([=|\/])\b([A-Z ][a-zA-Z ][a-zA-Z ]+)+\b\1"
raw_destinations = re.findall(expression, destinations)
valid_destinations = []
# print(raw_destinations)

for block in raw_destinations:
    valid_destinations.append(block[1])
    total_sum += len(block[1])

print(f"Destinations: "+ ', '.join(valid_destinations))
print(f"Travel Points: {total_sum}")
#RANGE v regeexa [a-zA-z ]{2,}
#finditer ako polzvame grupi 