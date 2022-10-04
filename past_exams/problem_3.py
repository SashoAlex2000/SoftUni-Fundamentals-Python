# Deck of Cards

deck = input().split(", ")
turns = int(input())

for turn in range(turns):
    line = input().split(", ")
    command = line[0]

    if command == "Add":
        card_name = line[1]
        if card_name in deck:
            print("Card is already in the deck")
        else:
            deck.append(card_name)
            print("Card successfully added")

    elif command == "Remove":
        card_name = line[1]
        if card_name not in deck:
            print("Card not found")
        else:
            deck.remove(card_name)
            print("Card successfully removed")

    elif command == "Remove At":
        index_to_remove = int(line[1])
        if 0 <= index_to_remove < len(deck):
            deck.pop(index_to_remove)
            print("Card successfully removed")
        else:
            print("Index out of range")

    elif command == "Insert":
        index_to_insert = int(line[1])
        card_name = line[2]
        if index_to_insert < 0 or index_to_insert >= len(deck):
            print("Index out of range")
        elif card_name in deck:
            print("Card is already added")
        else:
            deck.insert(index_to_insert, card_name)
            print("Card successfully added")

print(", ".join(deck))
