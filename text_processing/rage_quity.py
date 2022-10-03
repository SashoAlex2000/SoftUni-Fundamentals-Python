# ?????????

sequence = input()
turns = 0
current_string = ""
rage_output = []
unique_symbols = []


def rage_message(message, multiplier):
    message = message.upper()
    return message * multiplier


while turns < len(sequence):

    if not sequence[turns].isnumeric() and not sequence[turns].isdigit():
        current_string += sequence[turns]
        # turns += 1
        if sequence[turns].lower() not in unique_symbols:
            unique_symbols.append(sequence[turns].lower())
        turns += 1

    elif sequence[turns].isnumeric():
        number_multiplier = ""
        number_multiplier += sequence[turns]
        additive = 1
        for element in range(turns, len(sequence)):
            if turns == len(sequence) - 1 or turns + additive == len(sequence):
                break
            if sequence[turns + additive].isnumeric():
                if turns + additive < len(sequence):
                    number_multiplier += sequence[turns + additive]
            else:
                break
            additive += 1

        rage_output.append(rage_message(current_string, int(number_multiplier)))

        current_string = ""
        turns += 1

print(f"Unique symbols used: {len(unique_symbols)}")
print("".join(rage_output))
