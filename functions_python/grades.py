grades = float(input())

def grading(grade):

    if 2 <= grade < 3:
        return "Fail"
    elif grade < 3.49:
        return "Poor"
    elif grade < 4.49:
        return "Good"
    elif grade < 5.49:
        return "Very Good"
    else:
        return "Excellent"


print(grading(grades))
