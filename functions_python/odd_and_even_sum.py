
list_number = list(map(int, list(input())))


def odd_and_even(list):
    even_sum = 0
    odd_sum = 0
    for element in list:
        if element % 2 == 0:
            even_sum += element
        else:
            odd_sum += element
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")

odd_and_even(list_number)

