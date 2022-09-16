vowels = ["a","e", "i","o","u"]

word = input()

word_list = list(word)
# print(word_list)
new_list = []

for ch in word_list:
    if ch not in vowels:
        new_list.append((ch)

                        )

print("".join(new_list))

# ne e nujno da go pravim na list purvo