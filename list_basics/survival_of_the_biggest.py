number_input = input()
number_to_remove = int(input())
# int_list = list(map(int,number_input.split( )))
int_list = number_input.split(" ")
i = -1
for element in int_list:
    i += 1
    int_list[i] = int(element)



smallest_number = min(int_list)

for _ in range(number_to_remove):
    int_list.remove(min(int_list))

new_list = [str(x) for x in int_list]


print(", ".join(new_list))




