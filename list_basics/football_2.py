# import re

sequence = input()

new_list = sequence.split(" ")
# print(new_list)
cards_a = 0
cards_b = 0
a_list = []
b_list = []
is_cancelled = False

for element in new_list:
    new_element = "".join(i for i in element if i.isdigit())
    # print(new_element)
    if element[0] == "A" and new_element not in a_list:
        cards_a += 1
        a_list.append(new_element)

    elif element[0] == "B" and new_element not in b_list:
        cards_b += 1
        b_list.append(new_element)

if cards_a > 4 or cards_b > 4:
    is_cancelled = True

# difference_a = len(a_list) - len(set(a_list))
# print(difference_a)
# print(a_list)


print(f"Team A - {11 - cards_a}; Team B - {11 - cards_b}")
if is_cancelled:
    print("Game was terminated")