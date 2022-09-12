words = input()
water = int(input())
water1 = water

first_list = words.split("#")
total_efford = 0
numbers_list = []

for element in first_list:
    temporary_list = element.split(" ")

    if temporary_list[0] == "High":
        degrees = int(temporary_list[2])
        if 81 <= degrees < 126 and water >= degrees:
            water-= degrees
            total_efford += 0.25 * degrees
            numbers_list.append(temporary_list[2])

    elif temporary_list[0] == "Medium":
        degrees = int(temporary_list[2])
        if 51 <= degrees < 81 and water >= degrees:
            water-= degrees
            total_efford += 0.25 * degrees
            numbers_list.append(temporary_list[2])

    elif temporary_list[0] == "Low" and water >= degrees:
        degrees = int(temporary_list[2])
        if 1 <= degrees < 51:
            water-= degrees
            total_efford += 0.25 * degrees
            numbers_list.append(temporary_list[2])

print("Cells:")
for m in range(len(numbers_list)):
    print(" - ",end ="")
    print(numbers_list[m])



print(f"Effort: {total_efford:.2f}")
print(f"Total Fire: {water1 - water}")
