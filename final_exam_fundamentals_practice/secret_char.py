secret_message = input()

line = input()

while line != "Reveal":
    command = line.split(":|:")
    order = command[0]

    if order == "InsertSpace":
        indx = int(command[1])
        secret_message = secret_message[:indx]+ " " + secret_message[indx:]
        print(secret_message)

    elif order == "Reverse":
        substring = command[1]
        reversed_substring = substring[::-1]
        # reversed_substring = "asd"

        if substring in secret_message:
            secret_message = secret_message.replace(substring,"",1)
            secret_message = secret_message + reversed_substring
            print(secret_message)
        else:
            print("error")

    elif order == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        secret_message = secret_message.replace(substring,replacement)
        print(secret_message)

    line = input()

print(f"You have a new text message: {secret_message}")
