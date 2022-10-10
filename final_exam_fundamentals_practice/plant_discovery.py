number_of_lines = int(input())
plant_dict = {}

def rating_plants(ratings):
    plant_rating = 0
    curr_total = 0

    if len(ratings) > 1:
        for ratng in range(1,len(ratings)):
            curr_total += int(ratings[ratng])
        plant_rating = curr_total / (len(ratings) - 1)

    return plant_rating


for i in range(number_of_lines):
    first_line = input().split("<->")
    plant = first_line[0]
    rarity = first_line[1]
    # plant_dict[plant] = {rarity:[]}
    # plant_dict[plant][rarity] = i

    if plant not in plant_dict:
        plant_dict[plant] = [rarity]
    else:
        plant_dict[plant] = [rarity]

line = input()

while line != "Exhibition":
    command = line.split(": ")
    order = command[0]

    if order == "Rate":
        second_part = command[1].split(" - ")
        flower = second_part[0]
        rating = second_part[1]

        if flower in plant_dict:
            plant_dict[flower].append(rating)
        else:
            print(f"error")

    elif order == "Update":
        second_part = command[1].split(" - ")
        flower = second_part[0]
        new_rarity = second_part[1]

        if flower in plant_dict:
            plant_dict[flower][0] = new_rarity
        else:
            print(f"error")

    elif order == "Reset":
        flower = command[1]

        if flower in plant_dict:
            del plant_dict[flower][1:]
        else:
            print(f"error")

    line = input()


print(f"Plants for the exhibition:")
for plant, ratings in plant_dict.items():
    print(f"- {plant}; Rarity: {plant_dict[plant][0]}; Rating: {rating_plants(ratings):.2f}")