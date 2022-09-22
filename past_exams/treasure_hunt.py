treasure = input().split("|")

line = input()

while line != "Yohoho!":
    line_list = line.split(" ")
    command = line_list[0]

    if command == "Loot":
        for item in line_list[1:]:
            if item not in treasure:
                treasure.insert(0,item)

    elif command == "Drop":
        indexxx = int(line_list[1])
        if 0 < indexxx < len(treasure):
            thing_to_remove = treasure[indexxx]
            treasure.remove(thing_to_remove)
            treasure.append(thing_to_remove)

    elif command == "Steal":
        item_count = int(line_list[1])
        current_list = []

        if item_count >= len(treasure):
            # current_list.copy(treasure)
            current_list = treasure
            print(", ".join(current_list))
            treasure.clear()

        else:
            treasure.reverse()
            for i in range(item_count):
                current_list.append(treasure.pop(0))

            treasure.reverse()
            current_list.reverse()
            print(", ".join(current_list))
            current_list = []

    line = input()

# print(treasure)

total_coins = 0
for word in treasure:
    total_coins += len(word)

if len(treasure) > 0:
    print(f"Average treasure gain: {total_coins / len(treasure):.2f} pirate credits." )
else:
    print("Failed treasure hunt.")