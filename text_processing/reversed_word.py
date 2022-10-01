line = input()


# while line != "end":
#     lst = list(line)
#     lst.reverse()
#     print("".join(lst))
#
#     line = input()

while line != "end":
    for ch in reversed(line):
        print(ch, end ="")



    line = input()