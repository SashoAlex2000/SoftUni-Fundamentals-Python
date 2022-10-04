#Experience gaining

experience_needed = float(input())
count_of_battles = int(input())
total_experience = 0
enough_experience = False

for i in range(1, count_of_battles + 1):
    current_battle = float(input())

    if i % 3 == 0:
        current_battle *= 1.15
    if i % 5 == 0:
        current_battle *= 0.9
    if i % 15 == 0:
        current_battle *= 1.05

    total_experience += current_battle
    if total_experience >= experience_needed:
        enough_experience = True
        break

if enough_experience:
    print(f"Player successfully collected his needed experience for {i} battles.")
else:
    print(f"Player was not able to collect the needed experience, {experience_needed - total_experience:.2f} more needed.")


