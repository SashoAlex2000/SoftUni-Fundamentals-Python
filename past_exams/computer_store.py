total_price = 0
type_of_order = ""

command = input()
shouldnt_break = True

while shouldnt_break:
    if command == "special" or command == "regular":
        type_of_order = command
        shouldnt_break = False
        break
    command = float(command)
    if command < 0:
        print("Invalid price!")
    else:
        total_price += command

    command = input()
    # if command == "special" or command == "regular":
    #     type_of_order = command
    #     shouldnt_break = False

taxes = 0.2 * total_price
price_with_taxes = total_price + taxes

if total_price == 0:
    print("Invalid order!")
else:
    if type_of_order == "special":
        price_with_taxes *= 0.9
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total_price:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print("-----------")
        print(f"Total price: {price_with_taxes:.2f}$")
    elif type_of_order == "regular":
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total_price:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print("-----------")
        print(f"Total price: {price_with_taxes:.2f}$")




