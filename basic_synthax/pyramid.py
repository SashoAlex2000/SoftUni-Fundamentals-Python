# #? kek
number = int(input())

for i in range(1, number + 1):
    for n in range(0, i):
        print("*", end= "")
    print()


for i in range(number - 1, 0, -1):
    for k in range(0, i):
        print("*", end= "")
    print()



# number = int(input())
#
# for i in range(1, number + 1):
#     for n in range(1, i +1):
#         print("*" * n)
#
#
# for i in range(number - 1, 0, -1):
#     for k in range(0, i):
#         print("*", end= "")
#     print()
