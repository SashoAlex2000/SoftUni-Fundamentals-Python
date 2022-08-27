# word = input()
#
# # for ch in range(len(word),0 , -1):
#     # print(word[ch])
#
# for i in range(len(word) - 1, -1, -1):
#     print((word[i]).lower())

word = input()

reversed_word = ""

for i in range(len(word) -1, -1, -1):
    reversed_word += word[i]

print(reversed_word)