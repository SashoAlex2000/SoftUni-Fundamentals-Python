
import re
number_of_lines = int(input())
# expression = r"([@][#]+)([A-Z][A-Za-z0-9]{4,}[A-Z])([@][#]+)"
expression = r"[@][#]+[A-Z][A-Za-z0-9]{4,}[A-Z][@][#]+"

for turn in range(number_of_lines):
    thing = input()
    listtt = re.findall(expression,thing)
    barcode_list = []
    if len(listtt) == 0:
        print(f"Invalid barcode")
        continue


    for character in listtt[0]:
        if character.isdigit():
            barcode_list.append(character)

    if len(barcode_list) > 0:
        print("Product group: " + "".join(barcode_list))
    else:
        print("Product group: 00")



