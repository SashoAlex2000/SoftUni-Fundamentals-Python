sequence = list(input())
i = 0
required_explosions = sequence.count(">")
explosion_strength = 0
reserve = 0
done_explosions = 0
print(required_explosions)
indeces_to_destroy = []

while True:
    ch = sequence[i]
    ch_index = sequence.index(ch)
    if ch == ">":
        explosion_strength = sequence[ch_index + 1]
        # explosion_strength = int(explosion_strength)
        print(explosion_strength)
    explosion_strength = int(explosion_strength)
    if ch == ">" and explosion_strength == 1:
        indeces_to_destroy.append(ch_index + 1)
        done_explosions += 1

    elif ch == ">" and explosion_strength != 1:
        done_explosions += 1
        current_explosions = 0
        while True:
            if sequence[sequence.index(ch) + 1] != ">":
                current_explosions += 1
                indeces_to_destroy.append(sequence.index(ch) + 1 + current_explosions)

            elif sequence[sequence.index(ch) + 1] == ">":
                reserve += explosion_strength - current_explosions
                break

            if current_explosions >= explosion_strength:
                break

    if done_explosions >= required_explosions:
        break
    i += 1

print(sequence)
print(indeces_to_destroy)
