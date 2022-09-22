dungeon = input().split("|")
health = 100
bitcoins = 0
max_room = 0
journey_ended = False

for room in dungeon:
    room_list = room.split(" ")
    command = room_list[0]
    amount = int(room_list[1])

    if command == "potion":
        starting_health = health
        health += amount
        if health >= 100:
            health = 100
        print(f"You healed for {health - starting_health} hp.")
        print(f"Current health: {health} hp.")
        max_room += 1

    elif command == "chest":
        bitcoins += amount
        print(f"You found {amount} bitcoins.")
        max_room += 1

    else:
        health = health - amount
        max_room += 1
        if health > 0:
            print(f"You slayed {command}.")

        elif health <= 0:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {max_room}")
            journey_ended = True
            break


if not journey_ended:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")