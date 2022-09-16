
to_do = ["" for i in range(11)]
command = input()

while command != "End":
    explode = command.split("-")
    priority = int(explode[0])
    task = explode[1]
    to_do[priority] = task
    command = input()

result = [i for i in to_do if i != ""]
print(result)