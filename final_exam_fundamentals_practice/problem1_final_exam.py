
input_string = input()

line = input()

while line != "End":
    command = line.split(" ")

    order = command[0]

    if order == "Translate":
        char_to_replace = command[1]
        new_char = command[2]

        input_string = input_string.replace(char_to_replace,new_char)
        print(input_string)

    elif order == "Includes":
        string_toCheck = command[1]
        if string_toCheck in input_string:
            print("True")
        else:
            print("False")

    elif order == "Start":
        list_word = list(input_string)
        start_string = command[1]
        starts_with_String = True

        for char in start_string:
            current_index = start_string.index(char)
            if input_string[current_index] != char:
                starts_with_String = False

        if starts_with_String:
            print("True")
        else:
            print("False")

    elif order == "Lowercase":
        input_string = input_string.lower()
        print(input_string)

    elif order == "FindIndex":
        chart_to_search = command[1]
        index_of_char = input_string.rfind(chart_to_search)

        # for ch in input_string:
        #     if ch == chart_to_search:
        #         index_of_char = input_string.index(ch)

        print(index_of_char)

    elif order == "Remove":
        start_index = int(command[1])
        chars_to_remove = int(command[2])
        list_word = list(input_string)

        for i in range(chars_to_remove):
            list_word.pop(start_index)

        input_string = "".join(list_word)
        print(input_string)


    line = input()


# print(input_string)