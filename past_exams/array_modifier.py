sequence = list(map(int, input().split(" ")))

command = input()


while command != "end":
    command_list = command.split(" ")
    if command_list[0] == "swap":
        index1 = int(command_list[1])
        index2 = int(command_list[2])
        sequence[index2], sequence[index1] = sequence[index1], sequence[index2]

    elif command_list[0] == "multiply":
        index1 = int(command_list[1])
        index2 = int(command_list[2])
        booba = sequence[index1]
        booba *= sequence[index2]
        sequence[index1] = booba

    elif command_list[0] == "decrease":
        sequence = list(map(lambda n: n - 1, sequence))
        # for i in range(len(sequence)):
        #     integer = sequence[i]
        #     integer -= 1
        #     sequence[i] = integer


    command = input()
sequence = list(map(str, sequence))
print(", ".join(sequence))