days = int(input())

plunder_per_day = float(input())
goal_plunder = float(input())
days_so_far = 0
total_plunder = 0

for _ in range(days):
    days_so_far += 1
    total_plunder += plunder_per_day
    if days_so_far % 3 == 0:
        total_plunder += 0.5 * plunder_per_day

    if days_so_far % 5 == 0:
        total_plunder *= 0.7



if total_plunder >= goal_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {total_plunder/goal_plunder*100:.2f}% of the plunder.")

