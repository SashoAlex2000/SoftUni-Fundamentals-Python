targets = list(map(int, input().split(" ")))

command = input()

while command != "End":
    command = int(command)
    if command < 0 or command > len(targets) - 1:
        pass
    elif targets[command] == -1:
        pass
    else:
        target_shot_value = targets[command]

        for i in range(0,len(targets)):
            if targets[i] <= target_shot_value and targets[i] != -1:
                targets[i] += target_shot_value
            elif targets[i] > target_shot_value and targets[i] != -1:
                targets[i] -= target_shot_value

        targets[command] = -1

        #
        # for m in range(command + 1, len(targets)):
        #     if targets[m] < target_shot_value:
        #         targets[m] += target_shot_value
        #     elif targets[m] > target_shot_value:
        #         targets[m] -= target_shot_value
    command = input()

shot_targets = len([k for k in targets if k == -1])
targets = list(map(str, targets))
target_string = " ".join(targets)
print(f"Shot targets: {shot_targets} -> "+ target_string)