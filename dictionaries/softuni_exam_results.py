contest_dict = {}

line = input()

while line != "exam finished":
    command = line.split("-")

    if len(command) == 3:
        name = command[0]
        language = command[1]
        points = command[2]
        if name not in contest_dict:
            contest_dict[name] = []
            contest_dict[name].append({language:points})

        else:
            for lng in contest_dict[name]:
                if language not in




    if len(command) == 2:






    line = input()