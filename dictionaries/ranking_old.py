
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


        
# Test Input:  
#     #1
# Part One Interview:success
# JS Fundamentals:fundExam
# C# Fundamentals:fundPass
# Algorithms:fun
# end of contests
# C# Fundamentals=>fundPass=>Tanya=>350
# Algorithms=>fun=>Tanya=>380
# Part One Interview=>success=>Nikola=>120
# Java Basics Exam=>wrong_pass=>Teo=>400
# Part One Interview=>success=>Tanya=>220
# OOP Advanced=>password123=>Kay=>231
# C# Fundamentals=>fundPass=>Tanya=>250
# C# Fundamentals=>fundPass=>Nikola=>200
# JS Fundamentals=>fundExam=>Tanya=>400
# end of submissions

#     #2
# Java Advanced:funpass
# Part Two Interview:success
# Math Concept:asdasd
# Java Web Basics:forrF
# end of contests
# Math Concept=>ispass=>Monika=>290
# Java Advanced=>funpass=>Simona=>400
# Part Two Interview=>success=>Drago=>120
# Java Advanced=>funpass=>Petyr=>90
# Java Web Basics=>forrF=>Simona=>280
# Part Two Interview=>success=>Petyr=>0
# Math Concept=>asdasd=>Drago=>250
# Part Two Interview=>success=>Simona=>200
# end of submissions
