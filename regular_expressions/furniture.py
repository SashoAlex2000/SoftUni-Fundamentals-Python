import re

def furniture_info():
    pattern = r">>([a-zA-Z]+)<<(\d+|\d+\.+\d+)!(\d+)"
    total_expenditure = 0
    product_list = []

    while True:
        data = input()
        if data == "Purchase":
            break
        result = re.match(pattern,data)
        # print(result)

        if result != None:
            product = result[1]
            price = float(result[2])
            quantity = float(result[3])

            total_expenditure += price * quantity
            product_list.append(product)

    print(f"Bought furniture:")

    if total_expenditure > 0:
        print("\n".join(product_list))
    print(f"Total money spend: {total_expenditure:.2f}")
furniture_info()

