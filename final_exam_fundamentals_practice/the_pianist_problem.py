number_of_lines = int(input())
dict_composers = dict()

for i in range(number_of_lines):
    line = input().split("|")
    piece = line[0]
    composer = line[1]
    key_piece = line[2]

    dict_composers[piece] = [composer, key_piece]

# print(dict_composers)

command = input()

while command != "Stop":
    splittt = command.split("|")
    action = splittt[0]

    if action == "Add":
        current_piece = splittt[1]
        current_composer = splittt[2]
        current_key = splittt[3]

        if current_piece not in dict_composers.keys():
            dict_composers[current_piece] = [current_composer, current_key]
            print(f"{current_piece} by {current_composer} in {current_key} added to the collection!")

        else:
            print(f"{current_piece} is already in the collection!")

    elif action == "Remove":
        piece_to_remove = splittt[1]

        if piece_to_remove in dict_composers.keys():
            dict_composers.pop(piece_to_remove)
            print(f"Successfully removed {piece_to_remove}!")
        else:
            print(f"Invalid operation! {piece_to_remove} does not exist in the collection.")

    elif action == "ChangeKey":
        new_piece = splittt[1]
        new_key = splittt[2]

        if new_piece in dict_composers.keys():
            new_list = dict_composers[new_piece]
            new_list[1] = new_key
            dict_composers[new_piece] = new_list
            print(f"Changed the key of {new_piece} to {new_key}!")
        else:
            print(f"Invalid operation! {new_piece} does not exist in the collection.")

    command = input()

for piece, music_list in dict_composers.items():
    print(f"{piece} -> Composer: {music_list[0]}, Key: {music_list[1]}")
