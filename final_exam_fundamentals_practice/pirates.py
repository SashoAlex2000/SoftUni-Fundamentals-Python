towns_dict = {}

line = input()

while line != "Sail":
    command = line.split("||")
    town_name = command[0]
    population = int(command[1])
    gold = int(command[2])

    if town_name not in towns_dict:
        towns_dict[town_name] = [population,gold]
    else:
        towns_dict[town_name][0] += population
        towns_dict[town_name][1] += gold

    line = input()

line = input()

while line != "End":
    command = line.split("=>")
    order = command[0]

    if order == "Plunder":
        town = command[1]
        murdered_people = int(command[2])
        gold_stolen = int(command[3])

        towns_dict[town][0] -= murdered_people
        towns_dict[town][1] -= gold_stolen

        print(f"{town} plundered! {gold_stolen} gold stolen, {murdered_people} citizens killed.")

        if towns_dict[town][1] <= 0 or towns_dict[town][0] <= 0:
            print(f"{town} has been wiped off the map!")
            towns_dict.pop(town)
    elif order == "Prosper":
        town = command[1]
        added_gold = int(command[2])

        if added_gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            towns_dict[town][1] += added_gold
            print(f"{added_gold} gold added to the city treasury. {town} now has {towns_dict[town][1]} gold.")

    line = input()

if len(towns_dict) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(towns_dict)} wealthy settlements to go to:")
    for town, stats in towns_dict.items():
        print(f"{town} -> Population: {towns_dict[town][0]} citizens, Gold: {towns_dict[town][1]} kg")

