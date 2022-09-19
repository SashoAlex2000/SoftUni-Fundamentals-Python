archery = list(map(int, input().split(" ")))

command = input()
while command != "End":
    command_list = command.split(" ")
    indexx = int(command_list[1])
    power = int(command_list[2])
    if command_list[0] == "Shoot":

        if indexx < len(archery):
            if power < archery[indexx]:
                archery[indexx] -= power
            else:
                archery[indexx] = 0
                archery.pop(indexx)

    elif command_list[0] == "Add":
        if indexx < len(archery):
            value_to_insert = power
            archery.insert(indexx, value_to_insert)
        else:
            print("Invalid placement!")

    elif command_list[0] == "Strike":
        lower_range = indexx - power
        upper_range = indexx + power
        if lower_range >= 0 and upper_range < len(archery):
            del archery[lower_range:upper_range + 1]
        else:
            print("Strike missed!")

    command = input()

archery = list(map(str, archery))
print("|".join(archery))
