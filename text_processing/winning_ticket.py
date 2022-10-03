
list_tickets = [ticket for ticket in input().split(", ") if ticket != ""]
for i in range(len(list_tickets)):
    list_tickets[i] = list_tickets[i].strip()
    # print(list_tickets[i])

def check_ticket(ticket):
    ticket.strip()
    first_half = ticket[0:10]
    second_half = ticket[10:20]
    ticket_is_winning = False
    ticket_is_jackpot = False
    is_valid = False
    if len(ticket) == 20:
        is_valid = True

    if not is_valid:
        return f"invalid ticket"

    first_high_score = 0
    current_counter = 0
    current_letter = ""
    first_winning_symbol = ""

    for letter in first_half:
        if letter != current_letter:
            current_counter = 0
            current_letter = letter
        elif letter == current_letter:
            current_counter += 1

        if current_counter > first_high_score:
            first_high_score = current_counter
        if current_counter >= 5:
            first_winning_symbol = letter

    second_high_score = 0
    current_counter = 0
    current_letter = ""
    second_winning_symbol = ""

    for letter in second_half:
        if letter != current_letter:
            current_counter = 0
            current_letter = letter
        elif letter == current_letter:
            current_counter += 1

        if current_counter > second_high_score:
            second_high_score = current_counter
        if current_counter >= 5:
            second_winning_symbol = letter

    right_symbols = False
    if first_winning_symbol in ['@', '#', '$', '^' ] and second_winning_symbol in ['@', '#', '$', '^' ]:
        right_symbols = True
    if first_high_score >= 5 and second_high_score >= 5 and right_symbols:
        ticket_is_winning = True
    if first_high_score == 9 and second_high_score == 9 and right_symbols:
        ticket_is_winning = False
        ticket_is_jackpot = True

    if ticket_is_winning:
        return f'ticket "{ticket}" - {min(first_high_score, second_high_score) + 1}{first_winning_symbol}'
    elif ticket_is_jackpot:
        return f'ticket "{ticket}" - 10{first_winning_symbol} Jackpot!'
    else:
        return f'ticket "{ticket}" - no match'

# print(list_tickets)
for ticket in list_tickets:
    print(check_ticket(ticket))



