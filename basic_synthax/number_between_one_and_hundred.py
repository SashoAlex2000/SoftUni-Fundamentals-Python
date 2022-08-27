is_found = False

while not is_found:
    number = float(input())
    if number > 1 and number < 100:
        is_found = True


print(f"The number {number} is between 1 and 100")
