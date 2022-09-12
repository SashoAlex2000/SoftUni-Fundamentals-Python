from typing import List, Any

curr = input()

new_list = curr.split(" ")
cards_a = 0
cards_b = 0
red_flags_a = []
red_flags_b = []
game_was_terminated = False
print(new_list)

for element in curr:
    element_list: list[Any] = list(element)
    if element_list[0] == "A":
        if element_list[-1] not in red_flags_a:
            red_flags_a.append(element_list[-1])
            cards_a += 1


    elif element_list[0] == "B":
        if element_list[-1] != red_flags_b:
            red_flags_b.append(element_list[-1])
            cards_b += 1
    print(element_list)
    element_list = []


if cards_a > 5 or cards_b > 5:
    game_was_terminated = True

# difference_a = len(red_flags_a) - len(set(red_flags_a))
# difference_b = len(red_flags_b) - len(set(red_flags_b))

print(red_flags_a)
print(f"Team A - {11 - cards_a}; Team B - {11 - cards_b }")
if game_was_terminated:
    print("Game was terminated")
