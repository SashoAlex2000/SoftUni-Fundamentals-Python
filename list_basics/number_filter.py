lines = int(input())
list = []

for i in range(lines):
    number = int(input())
    list.append(number)

command = input()
new_list = []
if command == "even":
    for element in list:
        if element % 2 == 0:
            new_list.append(element)

elif command == "odd":
    for element in list:
        if element % 2 != 0:
            new_list.append(element)

elif command == "positive":
    for element in list:
        if element >= 0:
            new_list.append(element)

elif command == "negative":
    for element in list:
        if element < 0:
            new_list.append(element)

print(new_list)