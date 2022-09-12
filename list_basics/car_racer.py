initial_list = input().split(" ")
from math import floor
number_list = []

for i in initial_list:
    number_list.append(int(i))

steps = floor(len(number_list)/2)
left_driver = 0
right_driver = 0

for m in range(steps):
    if number_list[m] != 0:
        left_driver += number_list[m]
    else:
        left_driver *= 0.8

for n in range(1, steps + 1):
    if number_list[-n] != 0:
        right_driver += number_list[-n]
    else:
        right_driver *= 0.8

def winning_driver(x,y):
    return min(x,y)

winner = ""
if left_driver < right_driver:
    winner = "left"
else:
    winner = "right"

print(f"The winner is {winner} with total time: {winning_driver(left_driver,right_driver):.1f}")