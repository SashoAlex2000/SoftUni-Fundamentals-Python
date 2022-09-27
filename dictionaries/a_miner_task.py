# resources = {}
#
# command = input()

def miner_task():
    items\
        = {}

    while True:
        resource = input()
        if resource == "stop":
            break
        else:
            pass

        quantity = int(input())

        if resource not in items:
            items[resource] = quantity

        else:
            items[resource] += quantity

    for key, value in items.items():
        print(f"{key} -> {value}")


miner_task()


# while command != "Stop":
#     metal = command
#     quantity = int(input())
#
#
#
#     command = input()