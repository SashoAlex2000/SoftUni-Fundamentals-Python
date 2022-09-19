secret_message = input().split(" ")
deciphered_list = []

for word in secret_message:
    new_word = []
    first_letter = [i for i in word if i.isnumeric()]
    first_letter_str = int("".join(first_letter))
    new_first_letter = chr(first_letter_str)
    # print(new_first_letter)
    new_word.append(new_first_letter)

    str_word = [m for m in word if not m.isnumeric()]
    # print(str_word)
    str_word[0], str_word[-1] = str_word[-1] , str_word[0]
    for el in str_word:
        new_word.append(el)

    deciphered_list.append("".join(new_word))

print(" ".join(deciphered_list))
