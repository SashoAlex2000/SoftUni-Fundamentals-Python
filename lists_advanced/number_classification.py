number_List = list(map(int,input().split(", ")))
even_number = [num for num in number_List if num % 2 == 0]
odd_number = [num for num in number_List if num % 2 != 0]
positive_numbers = [num for num in number_List if num >= 0]
negative_numbers = [num for num in number_List if num < 0]

print(f"Positive: {', '.join(list(map(str,positive_numbers)))}")
print(f"Negative: {', '.join(list(map(str,negative_numbers)))}")
print(f"Even: {', '.join(list(map(str,even_number)))}")
print(f"Odd: {', '.join(list(map(str,odd_number)))}")