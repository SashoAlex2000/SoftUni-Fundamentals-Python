
first_list = input().split(", ")
int_list = []
zero_counter = 0
for x in first_list:
    int_list.append(int(x))
for y in int_list:
    if y == 0:
        zero_counter += 1


for i in range(zero_counter):
    int_list.remove(0)

for n in range(zero_counter):
    int_list.append(0)
print(int_list)


