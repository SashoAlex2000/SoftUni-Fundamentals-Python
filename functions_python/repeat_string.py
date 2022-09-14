input_string = input()
number_of_times = int(input())

def repeat_string(string, times):
    result = string * times
    return result


print(repeat_string(input_string,number_of_times))