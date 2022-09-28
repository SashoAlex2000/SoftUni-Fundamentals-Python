def phonebook_bonk(number_of_lines, phone_book_dicc):
    for x in range(number_of_lines):
        name = input()
        if name not in phone_book_dicc:
            print(f"Contact {name} does not exist.")
        else:
            print(f"{name} -> {phone_book_dicc[name]}")

    return True


def phonebook():
    phone_book_dicc = {}
    condition = False

    while True:
        contact_info = input().split("-")

        if contact_info[0].isdigit():
            condition = phonebook_bonk(int(contact_info[0]), phone_book_dicc)

        else:
            phone_book_dicc[contact_info[0]] = contact_info[1]

        if condition:
            break

phonebook()
