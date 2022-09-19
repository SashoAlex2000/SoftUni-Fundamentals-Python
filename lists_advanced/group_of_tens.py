initial_list = list(map(int, input().split(", ")))
from math import  floor
boundary = 0
iterations = floor(max(initial_list)/10)
current_digit = 0


while len(initial_list) > 0:
    boundary += 10
    current_list = []

    for i in range(1 , iterations + 1):

        for element in initial_list:
            if element <= boundary:
                current_list.append(element)
                initial_list.remove(element)

    current_digit += 1
    print(f"Group of {current_digit}0's: {current_list}")
