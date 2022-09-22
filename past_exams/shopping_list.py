groceries = input().split("!")

command = input()

while command != "Go Shopping!":
    command_list = command.split(" ")
    action = command_list[0]
    item = command_list[1]

    if action == "Urgent":
        if item not in groceries:
            groceries.insert(0, item)

    elif action == "Unnecessary":
        if item in groceries:
            groceries.remove(item)

    elif action == "Rearrange":
        if item in groceries:
            index_item = groceries.index(item)
            # groceries.insert(-1, groceries.pop(index_item))
            groceries.remove(item)
            groceries.append(item)

    elif action == "Correct":
        new_item = command_list[2]
        if item in groceries:
            index_item = groceries.index(item)
            groceries[index_item] = new_item


    command = input()

print(", ".join(groceries))



