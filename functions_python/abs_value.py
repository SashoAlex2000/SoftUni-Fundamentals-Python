sequence = input()
number_list = sequence.split(" ")

for i in range(len(number_list)):
    replacement = abs(float(number_list[i]))
    number_list[i] = replacement


print(number_list)