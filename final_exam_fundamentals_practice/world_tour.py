world_tour = input()

command = input()

while command != "Travel":
    split_command = command.split(":")
    order = split_command[0]

    if order == "Add Stop":
        indx = int(split_command[1])
        destination = split_command[2]

        if 0 <= (indx - 1) < len(world_tour):
            new_word = world_tour[0:indx] + destination +world_tour[indx:]
            world_tour = new_word

    elif order == "Remove Stop":
        start_index = int(split_command[1])
        end_index = int(split_command[2]) + 1

        if start_index in range(len(world_tour)) and (end_index - 1) in range(len(world_tour)):
        # if 0 <= start_index <= (end_index - 1) < len(world_tour):
            new_word = world_tour[0:start_index] + world_tour[end_index:]
            world_tour = new_word

    elif order == "Switch":
        old_string = split_command[1]
        new_string = split_command[2]

        if old_string in world_tour:
            new_word = world_tour.replace(old_string, new_string)
            world_tour = new_word

    print(world_tour)
    command = input()

print(f"Ready for world tour! Planned stops: {world_tour}")