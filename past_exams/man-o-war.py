pirate_ship = list(map(int, input().split(">")))
battleship = list(map(int, input().split(">")))
max_health = int(input())

line = input()
premature_ending = False

while line != "Retire":
    line_list = line.split(" ")
    command = line_list[0]

    if command == "Fire":
        indexx = int(line_list[1])
        damage = int(line_list[2])
        if 0 <= indexx < len(battleship):
            section = battleship[indexx]
            section -= damage
            if section <= 0:
                print("You won! The enemy ship has sunken.")
                premature_ending = True
                break
            battleship[indexx] = section

    elif command == "Defend":
        start_index = int(line_list[1])
        end_index = int(line_list[2])
        pirate_damage = int(line_list[3])

        if start_index >= 0 and end_index < len(pirate_ship):
            for i in range(start_index, end_index + 1):
                current_section = pirate_ship[i]
                current_section = current_section - pirate_damage
                if current_section <= 0:
                    print(f"You lost! The pirate ship has sunken.")
                    premature_ending = True
                    break
                pirate_ship[i] = current_section
                # print(pirate_ship)


    elif command == "Repair":
        repair_index = int(line_list[1])
        repair_health = int(line_list[2])

        if 0 <= repair_index < len(pirate_ship):
            current_health = pirate_ship[repair_index]
            current_health += repair_health
            if current_health >= max_health:
                current_health = max_health

            pirate_ship[repair_index] = current_health

    elif command == "Status":
        repairs_needed = 0
        for section in pirate_ship:
            if section < 0.2 * max_health:
                repairs_needed += 1

        print(f"{repairs_needed} sections need repair.")

    line = input()


if not premature_ending:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(battleship)}")