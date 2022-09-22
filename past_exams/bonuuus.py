number_of_students = int(input())
total_lectures = int(input())
bonus = int(input())
# import sys
import math

max_student = 0
best_students_courses = 0

for i in range(number_of_students):
    current_student = int(input())
    total_bonus = math.ceil((current_student / total_lectures) * (5 + bonus))

    if total_bonus >= max_student:
        max_student = total_bonus
        best_students_courses = current_student

print(f"Max Bonus: {max_student}.")
print(f"The student has attended {best_students_courses} lectures.")