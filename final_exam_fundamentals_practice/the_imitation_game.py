
word_list = list(input())


line = input()

while line != "Decode":
    command = line.split("|")
    # print(command)
    instruction = command[0]

    if instruction == "ChangeAll":
        old_letter = command[1]
        new_letter = command[2]

        word_string = "".join(word_list)
        word_string = word_string.replace(old_letter,new_letter)
        word_list = list(word_string)

        # for ch in word_list:
        #     if ch == old_letter:
        #         current_index = word_list.index(ch)
        #         word_list[current_index] = new_letter

    elif instruction == "Insert":
        indexx = int(command[1])
        character = command[2]
        if indexx <= len(word_list):
            word_list.insert(indexx,character)

    elif instruction == "Move":
        moves = int(command[1])
        if moves > 0:
            for i in range(moves):
                word_list.append(word_list.pop(0))

    line = input()

print("The decrypted message is: "+"".join(word_list))