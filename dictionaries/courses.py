course_dict = {}

line = input()

while line != "end":
    command = line.split(" : ")
    course = command[0]
    name = command[1]

    if course not in course_dict.keys():
        course_dict[course] = []
        course_dict[course].append(name)

    else:
        course_dict[course].append(name)

    line = input()

for course,student in course_dict.items():
    # print(f"{course}: {len(course_dict[course])}")
    print(f"{course}: {len(student)}")

    for std in student:
        print(f"-- {std}")


