lines = int(input())
word = input()
list = []
new_list = []

for _ in range(lines):
    curr = input()
    list.append(curr)

for element in list:
    if word in element:
        new_list.append(element)

print(list)
print(new_list)
