number_of_lines = int(input())
garage_dict = {}

for _ in range(number_of_lines):
    line = input().split("|")
    car = line[0]
    mileage = int(line[1])
    fuel = int(line[2])

    garage_dict[car] = [mileage,fuel]

line = input()

while line != "Stop":
    command = line.split(" : ")
    order = command[0]

    if order == "Drive":
        current_car = command[1]
        current_mileage = int(command[2])
        current_fuel = int(command[3])

        if current_fuel > garage_dict[current_car][1]:

            print(f"Not enough fuel to make that ride")
        else:
            garage_dict[current_car][1] -= current_fuel
            garage_dict[current_car][0] += current_mileage
            print(f"{current_car} driven for {current_mileage} kilometers. {current_fuel} liters of fuel consumed.")

            if garage_dict[current_car][0] >= 100000:
                print(f"Time to sell the {current_car}!")
                del garage_dict[current_car]

    elif order == "Refuel":
        current_car = command[1]
        fuel_refilled = int(command[2])
        initial_fuel = garage_dict[current_car][1]
        garage_dict[current_car][1] += fuel_refilled
        if garage_dict[current_car][1] > 75:
            garage_dict[current_car][1] = 75
        print(f"{current_car} refueled with {min(fuel_refilled,(75-initial_fuel))} liters")

    elif order == "Revert":
        current_car = command[1]
        decreased_mileage = int(command[2])

        garage_dict[current_car][0] -= decreased_mileage

        if garage_dict[current_car][0] < 10000:
            garage_dict[current_car][0] = 10000
        else:
            print(f"{current_car} mileage decreased by {decreased_mileage} kilometers")

    line = input()

for car, stats in garage_dict.items():
    print(f"{car} -> Mileage: {stats[0]} kms, Fuel in the tank: {stats[1]} lt.")