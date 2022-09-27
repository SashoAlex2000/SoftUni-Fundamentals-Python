storage = input().split(" ")
storage_dict = {}

for i in range(0, len(storage), 2):
    food_item = storage[i]
    quantity = storage[i+1]
    storage_dict[food_item] = int(quantity)

wanted_items = input().split(" ")

for item in wanted_items:
    if item in storage_dict.keys():
        print(f"We have {storage_dict[item]} of {item} left")

    else:
        print(f"Sorry, we don't have {item}")

