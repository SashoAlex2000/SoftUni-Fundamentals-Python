
follower_dict = {}

line = input()

while line != "Log out":
    command = line.split(": ")

    order = command[0]

    if order == "New follower":
        new_user = command[1]
        if new_user not in follower_dict.keys():
            follower_dict[new_user] = [0, 0]

    elif order == "Like":
        user = command[1]
        like_count = int(command[2])

        if user not in follower_dict:
            follower_dict[user] = [like_count, 0]
        else:
            follower_dict[user][0] += like_count

    elif order == "Comment":
        user = command[1]

        if user not in follower_dict:
            follower_dict[user] = [0,1]
        else:
            follower_dict[user][1] += 1

    elif order == "Blocked":
        username = command[1]

        if username in follower_dict:
            del follower_dict[username]
        else:
            print(f"{username} doesn't exist.")


    line = input()

print(f"{len(follower_dict)} followers")
for follower, stats in follower_dict.items():
    print(f"{follower}: {stats[0] + stats[1]}")