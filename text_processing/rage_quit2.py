sequence = input()
turns = 0
current_string = ""
current_number = ""
rage_output = []
unique_symbols = []


def rage_message(message, multiplier):
    message = message.upper()
    return message * multiplier


letter_sequence = []
for symbol in sequence:
    if not symbol.isnumeric():
        letter_sequence.append(symbol)
        if symbol.lower() not in unique_symbols:
            unique_symbols.append(symbol.lower())
    elif symbol.isnumeric():
        letter_sequence.append("!")

final_letter_sequence = []
current_letters = ""

while turns < len(letter_sequence):
    cic = letter_sequence[turns]

    if not cic.isnumeric() and cic != "!":
        current_letters += cic
    elif cic == "!":
        final_letter_sequence.append(current_letters)
        current_letters = ""

    turns += 1

print(final_letter_sequence)
turns = 0

number_sequence_final = []
sequence_list = list(sequence)
current_number = ""

number_sequence = [symbol if symbol.isnumeric() else "c" for symbol in sequence]

while turns < len(number_sequence):
    kur = number_sequence[turns]

    if kur.isnumeric():
        current_number += kur
    elif kur == "c":
        number_sequence_final.append(current_number)
        current_number = ""

    turns += 1

for symbol in number_sequence_final:
    if symbol == "":
        number_sequence_final.remove(symbol)

print(number_sequence_final)

