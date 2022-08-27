name = input()

is_love = False
thing_to_print = ""
if name == "Johnny":
    is_love = True

if is_love:
    thing_to_print = "my love"
else:
    thing_to_print = name

print(f"Hello, {thing_to_print}!")