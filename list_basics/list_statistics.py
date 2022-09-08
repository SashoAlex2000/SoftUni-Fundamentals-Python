number = int(input())
positive_count = 0
negative_sum = 0
positive_list = []
negative_list = []

for i in range(number):
    curr = int(input())
    if curr >= 0:
        positive_count += 1
        positive_list.append(curr)
    else:
        negative_sum += curr
        negative_list.append(curr)

print(positive_list)
print(negative_list)
print(f"Count of positives: {positive_count}")
print(f"Sum of negatives: {negative_sum}"
      )
