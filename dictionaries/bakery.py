data = input().split(" ")

dicc = dict()

for i in range(0, len(data,) ,2):
    food = data[i]
    quantity = data[i+1]
    dicc[food] = int(quantity)

print(dicc)

for (key,value) in dicc.items():
    print(f"Key: {key} ; Value: {value}")