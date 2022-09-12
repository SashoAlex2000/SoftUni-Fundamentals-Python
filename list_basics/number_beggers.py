
sequence = input()
# new_sequence = "".join(i for i in sequence if i.isdigit())

number_of_beggars = int(input())

list = sequence.split(", ")
print(list)
outcome_list = []
m = -1




for number in list:
    outcome_list.append(number)


print(outcome_list)
