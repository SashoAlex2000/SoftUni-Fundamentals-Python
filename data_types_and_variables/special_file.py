
number = int(input())
is_special = False

for i in range(1, number + 1
               ):
    current_sum = 0
    for digit in str(i):
        current_sum += int(digit)

    if current_sum == 5 or current_sum == 7 or current_sum == 11:
        is_special = True
    else:
        is_special = False

    if is_special:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")





