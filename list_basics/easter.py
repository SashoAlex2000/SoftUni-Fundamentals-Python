gifts = input()

list_of_gifts = gifts.split(" ")
# print(list_of_gifts)

command = input()

while command != "No Money":
    current_list = command.split(" ")
    counter = -1
    if current_list[0] == "OutOfStock":
        none_word = None
        word_to_remove = current_list[1]
        for word in list_of_gifts:
            counter += 1
            if word == word_to_remove:
                list_of_gifts[counter] = none_word




    elif current_list[0] == "Required":
        if int(current_list[2]) <= len(list_of_gifts) - 1:
            index = int(current_list[2])
            i = current_list[1]
            list_of_gifts[index] = i

    elif current_list[0] == "JustInCase":
        list_of_gifts[-1] = current_list[1]

    current_list = []
    command = input()
    counter = -1

new_list = [x for x in list_of_gifts if x != None]
print(" ".join(new_list))


