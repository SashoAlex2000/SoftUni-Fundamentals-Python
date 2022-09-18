def is_even(word):
    if len(word) % 2 == 0:
        return True
    return  False

words = list(filter(is_even, input().split(" ")))
print("\n".join(words))