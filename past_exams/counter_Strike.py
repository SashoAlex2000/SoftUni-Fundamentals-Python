energy = int(input())

battles_won = 0

command = input()
energy_is_over = False

while command != "End of battle":
    distance = int(command)
    if energy < distance:
        energy_is_over = True
        break

    else:
        energy -= distance
        battles_won += 1

    if battles_won % 3 == 0:
        energy += battles_won

    command = input()

if energy_is_over:
    print(f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy")
else:
    print(f"Won battles: {battles_won}. Energy left: {energy}")