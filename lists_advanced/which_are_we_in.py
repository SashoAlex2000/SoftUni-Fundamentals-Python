first_list = input().split(", ")
second_list = input().split(", ")

special_list = []

for word in first_list:
    for element in second_list:
        if word in element:
            special_list.append(word)
            break

final_list = list(set(special_list))

print(special_list)
