lines_number = int(input())

parking_dict = {}

for turn in range(lines_number):
    command = input().split(" ")
    name = command[1]

    if command[0] == "register":
        licence_plate = command[2]
        if name not in parking_dict:
            parking_dict[name] = licence_plate
            print(f"{name} registered {licence_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking_dict[name]}")

    elif command[0] == "unregister":
        if name in parking_dict:
            parking_dict.pop(name)
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")


for key, value in parking_dict.items():
    print(f"{key} => {value}")



