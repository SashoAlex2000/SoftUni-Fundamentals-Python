text = input()
store = dict()

while text != "statistics":
    text = text.split(": ")
    product = text[0]
    quantity = int(text[1])

    if product not in store:
        store[product] = quantity
    else:
        store[product] += quantity

    text = input()

count = len(store.keys())
total = sum(store.values())

print(f"Products in stock: ")

for product_f in store.keys():
    print(f"- {product_f}: {store[product_f]}")

print(f"Total Products: {count}")
print(f"Total Quantity: {total}")
