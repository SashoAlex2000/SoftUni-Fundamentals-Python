
# from math import ceil
legendary_items_dict = {"shards": 0, "fragments": 0, "motes": 0}
junk_items = {}
time_to_break = False
special_item = ""

while True:
    command = input().lower()

    command = command.split(" ")
    for quantity, material in zip(command[0::2], command[1::2]):
        quantity = int(quantity)
        material = material.lower()

        if material in ["shards", "fragments", "motes"]:
            # if material not in legendary_items_dict:
            #     legendary_items_dict[material] = quantity
            # else:
            legendary_items_dict[material] += quantity

            if legendary_items_dict[material] >= 250:
                time_to_break = True

                if material == "shards":
                    special_item = "Shadowmourne"
                elif material == "fragments":
                    special_item = "Valanyr"
                elif material == "motes":
                    special_item = 'Dragonwrath'
                # print(special_item)
                legendary_items_dict[material] -= 250
        else:
            if material not in junk_items:
                junk_items[material] = quantity
            elif material in junk_items:
                junk_items[material] += quantity
        if time_to_break:
            break
    if time_to_break:
        break

print(f"{special_item} obtained!")
print(f"shards: {legendary_items_dict['shards']}")
print(f"fragments: {legendary_items_dict['fragments']}")
print(f"motes: {legendary_items_dict['motes']}")

for key, value in junk_items.items():
    print(f"{key}: {value}")