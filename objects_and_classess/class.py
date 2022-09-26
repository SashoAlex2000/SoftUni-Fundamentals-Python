class Class:
    __students_count = 22

    def __init__(self, name_of_class):
        self.name_of_class = name_of_class
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        average_grade = sum(self.grades) / len(self.students)
        return average_grade

    def __repr__(self):
        return f"The students in {self.name_of_class}: {', '.join(self.students)}. Average grade: {self.get_average_grade():.2f}"

a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
