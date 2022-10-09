

password = input()

line = input()

while line != "Done":
    command = line.split(" ")
    order = command[0]

    if order == "TakeOdd":
        new_pass = ""
        for i in range(len(password)):
            if i % 2 != 0:
                new_pass += password[i]

        password = new_pass
        print(password)

    elif order == "Cut":
        indx = int(command[1])
        length = int(command[2])
        pass_list = list(password)
        pass_list = pass_list[0:indx] + pass_list[(indx + length):]
        password = "".join(pass_list)
        print(password)

    elif order == "Substitute":
        substring = command[1]
        substitute = command[2]

        if substring in password:
            password = password.replace(substring,substitute)
            print(password)
        else:
            print(f"Nothing to replace!")


    line = input()

print(f"Your password is: {password}")
