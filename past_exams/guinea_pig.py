food = float(input())
hay = float(input()) * 1000
cover = float(input()) * 1000
weight = float(input()) * 1000
food *= 1000

has_failed = False
i = 0


for i in range(1, 31):
    food -= 300
    if food <= 0:
        has_failed = True
    if i % 2 == 0:
        hay -= 0.05 * food
        if hay <= 0:
            has_failed = True
    if i % 3 == 0:
        cover -= (weight/3)
        if cover <= 0:
            has_failed = True


if not has_failed:
    print(f"Everything is fine! Puppy is happy! Food: {food/1000:.2f}, Hay: {hay/1000:.2f}, Cover: {cover/1000:.2f}.")
else:
    print(f"Merry must go to the pet store!")

