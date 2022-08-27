number = float(input())

is_small = False
is_large = False

if abs(number) < 1 and number != 0:
    is_small = True

if abs(number) > 1000000:
    is_large = True

if number == 0:
    print("zero")

elif number < 0:
    if is_small:
        print("small negative")
    elif is_large:
        print("large negative")
    else:
        print("negative")

elif number > 0:
    if is_small:
        print("small positive")
    elif is_large:
        print("large positive")
    else:
        print("positive")
