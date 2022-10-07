raw_string = input()

line = input()


while line != "Generate":
    command = line.split(">>>")
    order = command[0]

    if order == "Contains":
        substring = command[1]
        if substring in raw_string:
            print(f"{raw_string} contains {substring}")
        else:
            print(f"Substring not found!")

    elif order == "Flip":
        formatting = command[1]
        start_idndex = int(command[2])
        end_idndex = int(command[3])
        substring = raw_string[start_idndex:end_idndex]
        if formatting == "Upper":
            substring= substring.upper()
        elif formatting == "Lower":
            substring= substring.lower()
        raw_string = raw_string[0:start_idndex] + substring + raw_string[end_idndex:]
        print(raw_string)

    elif order == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        raw_string = raw_string[0:start_index] + raw_string[end_index:
                                                 ]

        print(raw_string)

    line = input()

print(f"Your activation key is: {raw_string}")