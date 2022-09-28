lines_of_input = int(input())

students_dict = {}
final_dict = {}

for _ in range(lines_of_input):
    name = input()
    grade = float(input())

    if name not in students_dict.keys():
        students_dict[name] = []
        students_dict[name].append(grade)
    else:
        students_dict[name].append(grade)

for student, grades in students_dict.items():
    average_grade = sum(grades)/ len(grades)
    if average_grade >= 4.5:
        final_dict[student] = average_grade
    else:
        pass

for student, avg_grd in final_dict.items():
    print(f"{student} -> {avg_grd:.2f}")