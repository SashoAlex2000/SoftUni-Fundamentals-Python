lines = int(input())
game_is_on = True
free_chairs = 0

for i in range(1,  lines + 1):
    current_room = input().split(" ")
    # print(current_room)
    chairs = len(current_room[0])
    # print(chairs)
    guests = int(current_room[1])
    # print(guests)

    if chairs < guests:
        print(f"{guests - chairs} more chairs needed in room {i}")
        game_is_on = False
    else:
        free_chairs = free_chairs + chairs - guests


if game_is_on:
    print(f"Game On, {free_chairs} free chairs left")