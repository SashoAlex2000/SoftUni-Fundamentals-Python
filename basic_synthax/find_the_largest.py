number = int(input())

number = str(number)
empty_list = []

for ch in number:
    empty_list.append(ch)

empty_list.sort(reverse=True)
answer = ""

# for element in empty_list:
#     answer.join(element)


# for i in empty_list:
#     print(i, end="")

def convert(empty_list):
    res = int("".join(map(str,empty_list)))
    return res

print(convert(empty_list))