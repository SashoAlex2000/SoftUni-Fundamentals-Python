word_list = input().split(" ")

word1 = word_list[0]
word2 = word_list[1]
total_sum = 0

length = len(min(word_list, key=len))
# print(length)

for turn in range(length):
    current_result = ord(word1[turn]) * ord(word2[turn])
    total_sum += current_result

# print(total_sum)

if len(word1) > length:
    for ch in range(length, len(word1)):
        total_sum += ord(word1[ch])

if len(word2) > length:
    for ch in range(length, len(word2)):
        total_sum += ord(word2[ch])

print(total_sum)



