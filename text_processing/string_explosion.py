explosion = list(input())
i=0
number_of_explosions = explosion.count(">")

done_explosions = 0
reserve = 0

while True:
    current_char = explosion[i]

    if current_char == ">":
        done_explosions += 1
        explosion_strength = int(explosion[i+1]) + reserve
        lower_limit = i + 1
        # print(lower_limit)
        current_bombs = 0

        for cic in range(lower_limit, lower_limit + explosion_strength):
            if explosion[cic] != ">":
                explosion.pop(cic)
                current_bombs += 1
            else:
                reserve += (explosion_strength - done_explosions)
                break
    i += 1
    if done_explosions >= number_of_explosions:
        break


print(explosion)
