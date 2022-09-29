
contests = input()
dict_contests = {}

while contests != "end of contests":
    (contest, password) = contests.split(":")
    dict_contests[contest] = password

    contests = input()

# print(dict_contests)


submission_data = input()
user_dict = {}

while submission_data != "end of submissions":
    (contest, password, user, points) = submission_data.split("=>")
    if contest in dict_contests.keys():
        if dict_contests[contest] == password:
            if user not in user_dict:
                user_dict[user] = {}
            if contest in user_dict[user] and user_dict[user][contest] < int(points):
                user_dict[user][contest] = int(points)
            elif contest not in user_dict[user]:
                user_dict[user][contest] = int(points)


    submission_data = input()

best_user = ""
best_points = 0

for user in user_dict:
    total_points = sum(user_dict[user].values())
    if total_points > best_points:
        best_points = total_points
        best_user = user

print(f"Best candidate is {best_user} with total {best_points} points.")
print(f"Ranking:")
for user in sorted(user_dict.keys()):
    print(user)
    for contest,points in sorted(user_dict[user].items(), key = lambda cp: -cp[1]):
        print(f"#  {contest} -> {user_dict[user][contest]}")

