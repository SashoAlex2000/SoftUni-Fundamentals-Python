companies_dict = {}

line = input()

while line != "End":
    command = line.split(" -> ")
    company = command[0]
    id_number = command[1]

    if company not in companies_dict.keys():
        companies_dict[company] = []
        if id_number not in companies_dict[company]:
            companies_dict[company].append(id_number)

    else:
        if id_number not in companies_dict[company]:
            companies_dict[company].append(id_number)

    line = input()

for comp, employees in companies_dict.items():
    print(f"{comp}")
    for empl in employees:
        print(f"-- {empl}")