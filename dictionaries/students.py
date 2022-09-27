text = input()
courses = dict()

while ":" in text:
    (name, id, course_name) = text.split(":")
    #
    # data = text.split(":")
    # name = data[0]
    # id = data[1]
    # course_name = data[2]

    if course_name not in courses.keys():
        courses[course_name] = dict()

    courses[course_name][id] = name


    text = input()
text = " ".join(text.split("_"))
#python replace char

for id in courses[text]:
    print(f"{courses[text][id]} - {id}")