import math

sequence = input().split(" ")
sequence = [string for string in sequence if string != ""]
from math import floor
command = input()
player_has_failed = False
number_of_moves = 0

while True:
    if len(sequence) == 0:
        player_has_failed = False
        break
    if command == "end":
        player_has_failed = True
        break

    number_of_moves += 1
    command_list = command.split(" ")
    index1 = int(command_list[0])
    index2 = int(command_list[1])
    if index2 >= len(sequence) or index1 >= len(sequence) or index1 < 0 or index2 < 0 or index1 == index2:
        thing_to_add = f"-{number_of_moves}a"
        index_to_add = math.floor(len(sequence) / 2)
        sequence.insert(index_to_add, thing_to_add)
        sequence.insert(index_to_add, thing_to_add)

        print("Invalid input! Adding additional elements to the board")

    else:
        if sequence[index2] == sequence[index1]:
            print(f"Congrats! You have found matching elements - {sequence[index1]}!")
            thing_to_remove = sequence[index1]
            sequence.remove(thing_to_remove)
            sequence.remove(thing_to_remove)
        else:
            print("Try again!")

    command = input()

if player_has_failed:
    print("Sorry you lose :("
          )
    print(" ".join(sequence))
else:
    print(f"You have won in {number_of_moves} turns!")
