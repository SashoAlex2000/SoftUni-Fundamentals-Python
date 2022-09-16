wagons = int(input())
#purvo reshavame neshtata, posle mislim dali moje da se optimizira -> kato junior
wagon_list = [0] * wagons
# print(wagon_list)
last_wagon = len(wagon_list) - 1
command = input()

while command != "End":
    command_list = command.split(" ")
    if command_list[0] == "add":
        last_wagon_count = int(wagon_list[last_wagon])
        last_wagon_count += int(command_list[1])
        wagon_list[last_wagon] = int(last_wagon_count)
    elif command_list[0] == "insert":
        current_wagon = int(wagon_list[int(command_list[1])])
        current_wagon += int(command_list[2])
        wagon_list[int(command_list[1])] = current_wagon
    elif command_list[0] == "leave":
        current_wagon = int(wagon_list[int(command_list[1])])
        current_wagon -= int(command_list[2])
        wagon_list[int(command_list[1])] = current_wagon
    command = input()

print(wagon_list)
