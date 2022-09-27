words = input().split(" ")
words_copy = words.copy()
words = list(map(lambda w: w.lower(), words))
#
# new_words = [word.lower() for word in words_copy]
# print(words)
# print(new_words)
occurrences = dict()

for word in words:
    if word not in occurrences:
        occurrences[word] = 1
    else:
        occurrences[word] += 1
new_fag = []
for key in occurrences.keys():
    if occurrences[key] % 2 != 0:
        new_fag.append(key)

new_fag = list(map(str, new_fag))

print(" ".join(new_fag))