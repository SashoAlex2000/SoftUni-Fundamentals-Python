#tax calculator

caravan = input().split(">>")
total_taxes = 0
from math import floor

for car in caravan:
    car_list = car.split(" ")
    command = car_list[0]
    years = int(car_list[1])
    kilometers = int(car_list[2])
    current_tax = 0
    invalid_type = False

    if command == "family":
        current_tax = 50
        current_tax -= years * 5
        current_tax += floor(kilometers / 3000) * 12

    elif command == "heavyDuty":
        current_tax = 80
        current_tax -= years * 8
        current_tax += floor(kilometers / 9000) * 14

    elif command == "sports":
        current_tax = 100
        current_tax -= years * 9
        current_tax += floor(kilometers / 2000) * 18

    else:
        invalid_type = True

    total_taxes += current_tax
    if invalid_type:
        print("Invalid car type.")
    else:
        print(f"A {command} car will pay {current_tax:.2f} euros in taxes.")

print(f"The National Revenue Agency will collect {total_taxes:.2f} euros in taxes.")

