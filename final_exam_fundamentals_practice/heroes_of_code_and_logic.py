number_of_heroes = int(input())
heroes_dict = {}

for _ in range(number_of_heroes):
    line = input().split(" ")
    hero_name = line[0]
    hp = int(line[1])
    mana = int(line[2])
    heroes_dict[hero_name] = [hp, mana]

line = input()

while line != "End":
    command = line.split(" - ")
    order = command[0]

    if order == "CastSpell":
        hero_name = command[1]
        mana_needed = int(command[2])
        spell_name = command[3]

        if mana_needed <= heroes_dict[hero_name][1]:
            heroes_dict[hero_name][1] -= mana_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name][1]} MP!")

        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif order == "TakeDamage":
        hero_name = command[1]
        damage_taken = int(command[2])
        attacker = command[3]
        heroes_dict[hero_name][0] -= damage_taken

        if heroes_dict[hero_name][0] <= 0:
            print(f"{hero_name} has been killed by {attacker}!")
        else:
            print(f"{hero_name} was hit for {damage_taken} HP by {attacker} and now has {heroes_dict[hero_name][0]} "
                  f"HP left!")

    elif order == "Recharge":
        hero_name = command[1]
        restored_mana = int(command[2])
        beginning_mana = heroes_dict[hero_name][1]
        heroes_dict[hero_name][1] += restored_mana

        if heroes_dict[hero_name][1] > 200:
            heroes_dict[hero_name][1] = 200

        print(f"{hero_name} recharged for {min(restored_mana, (200 - beginning_mana))} MP!")

    elif order == 'Heal':
        hero_name = command[1]
        heal_amount = int(command[2])
        beginning_health = heroes_dict[hero_name][0]

        heroes_dict[hero_name][0] += heal_amount

        if heroes_dict[hero_name][0] > 100:

            heroes_dict[hero_name][0] = 100

        print(f"{hero_name} healed for {min(heal_amount, (100 - beginning_health))} HP!")

    line = input()

for hero, stats in heroes_dict.items():
    if stats[0] > 0:
        print(f"{hero}")
        print(f"  HP: {stats[0]}")
        print(f"  MP: {stats[1]}")



