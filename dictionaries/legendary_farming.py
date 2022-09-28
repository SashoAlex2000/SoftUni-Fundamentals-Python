def print_funct(legendary_items_dict, junk_items, special_item):
    print(f"{special_item} obtained")
    print(f"shards: {legendary_items_dict['shards']}")
    print(f"fragments: {legendary_items_dict['fragments']}")
    print(f"motes: {legendary_items_dict['motes']}")

    for key, value in junk_items.items():
        print(f"{key} - {value}")


def legendary_tems():
    legendary_items_dict = {"shards": 0, "fragments": 0, "motes": 0}

    junk_items = {}
    while_condition = False
    while True:
        items = input().lower()
        items = input().split(" ")
        # print(zip(items[0::2], items[1::2]))
        for value, material in zip(items[0::2], items[1::2]):
            material = material.lower()
            value = int(value)

            if material in ["shards", "fragments", "motes"]:
                # if material not in legendary_items_dict:
                #     legendary_items_dict[material] = value
                # else:
                legendary_items_dict[material] += value

                if int(legendary_items_dict[material]) >= 250:
                    legendary_items_dict[material] -= 250
                    special_item = ""
                    if material == "shards":
                        special_item = "Shadowmourne"
                    elif material == "fragments":
                        special_item = "Valantyr"
                    elif material == "motes":
                        special_item = 'Dragonwrath'

                    print_funct(legendary_items_dict, junk_items, special_item)
                    while_condition = True

            else:
                if material not in junk_items:
                    junk_items[material] = value

                else:
                    junk_items[material] += value

            if while_condition:
                break
        if while_condition:
            break

#slice notation
legendary_tems()