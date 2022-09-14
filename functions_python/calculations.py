input_operator = input()

first_num = int(input())
second_num = int(input())

def sloving_cases(a,b,operator):
    result = None
    if operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b
    elif operator == 'divide':
        result = int(a/b)
    else:
        result = a*b

    return result

print(sloving_cases(first_num,second_num,input_operator))