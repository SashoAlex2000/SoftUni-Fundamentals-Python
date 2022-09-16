command = input()
priority_list = [0] * 10


while command != "End":
    command_list = command.split("-")
    index = int(command_list[0]) - 1
    task = str(command_list[1])
    priority_list.pop(index)
    priority_list.insert(index,task)
    command = input()

result = [shit for shit in priority_list if shit != 0]


print(result)

