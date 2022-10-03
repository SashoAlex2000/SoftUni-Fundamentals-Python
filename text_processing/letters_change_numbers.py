import string
# print(string.ascii_lowercase.index('b'))
total_sum = 0
game_letters = [hui for hui in input().split(" ") if hui != "" and hui != " "]
# print(game_letters)

def letter_position(letter):
    if letter.islower():
        return string.ascii_lowercase.index(letter) + 1
    elif letter.isupper():
        return string.ascii_uppercase.index(letter) + 1


for sequence in game_letters:
    first_letter = sequence[0]
    last_letter = sequence[-1]
    number = int("".join(c for c in sequence if c.isdigit()))
    first_letter_position = letter_position(first_letter)
    last_letter_position = letter_position(last_letter)

    if first_letter.islower():
        number = number * first_letter_position

    elif first_letter.isupper():
        number = number / first_letter_position

    if last_letter.isupper():
        number -= last_letter_position

    elif last_letter.islower():
        number += last_letter_position

    total_sum += number

print(f"{total_sum:.2f}")




