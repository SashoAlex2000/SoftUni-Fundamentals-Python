#lift4e

people = int(input())
lift = list(map(int, input().split(" ")))
limit = len(lift) * 4
shouldnt_break = True
people_on_lift = 0

# while True:
#     if people == 0:
#         break
#     if people_on_lift == limit:
#         break
# print(lift)
i = -1
for cabin in lift:
    i += 1
    if people > 0:
        people_to_add = min(4 - cabin, people)
        lift[i] += people_to_add
        people -= people_to_add
    else:
        pass

sum_of_lift = sum(lift)
lift = list(map(str, lift))
if people == 0 and sum_of_lift != limit:
    print(f"The lift has empty spots!")
    print(" ".join(lift)
          )
elif people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(" ".join(lift))

elif people == 0 and sum_of_lift == limit:
    print(" ".join(lift))
