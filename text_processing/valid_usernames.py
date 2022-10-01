initial_data = input().split(", ")
correct_usernames = []

for username in initial_data:
    is_valid = True
    if len(username) < 3 or  len(username) > 16:
        is_valid = False

    stripped_username = username.strip()
    if len(username) != len(stripped_username):
        is_valid = False

    for ch in username:
        if ch.isalpha() or ch.isnumeric():
            pass
        else:
            if ch == "_" or ch == "-":
                pass
            else:
                is_valid = False

    if is_valid:
        correct_usernames.append(username)

print(f"\n".join(correct_usernames))


