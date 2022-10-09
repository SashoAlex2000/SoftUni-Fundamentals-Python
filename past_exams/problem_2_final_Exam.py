import re

regex = r"(.+)[>]([0-9]{3})[\|]([a-z]{3})[\|]([A-Z]{3})[\|]([^<>]{3})<\1"
number_of_lines = int(input())


for turn in range(number_of_lines):
    line = input()

    length_check = re.findall(regex,line)
    if len(length_check) == 0:
        print('Try another password!')
        continue

    current_password = re.finditer(regex,line)
    list_password = []
    for match in current_password:
        numbers = match.group(2)
        lower_letters = match.group(3)
        upper_letters = match.group(4)
        symbols = match.group(5)

        list_password.append(numbers)
        list_password.append(lower_letters)
        list_password.append(upper_letters)
        list_password.append(symbols)

    print("Password: " + "".join(list_password))




# passwords = re.finditer(regex,line)
# for block in passwords:
#     print(block.group(1))
