version = list(map(int, input().split(".")))

if version[2] <= 8:
    version[2] += 1
    print(f"{version[0]}.{version[1]}.{version[2]}")
elif version[2] == 9:
    if version[1] <= 8:
        version[2] = 0
        version[1] += 1
        print(f"{version[0]}.{version[1]}.{version[2]}")
    elif version[1] == 9:
        version[2] = 0
        version[1] = 0
        version[0] += 1
        print(f"{version[0]}.{version[1]}.{version[2]}")


