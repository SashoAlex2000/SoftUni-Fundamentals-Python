import re

initial_text = input()
regex = r"([@#])\b(?P<word1>[a-zA-Z]+)\1\1(?P<word2>[a-zA-Z]+)\b\1"

filtered_words = re.finditer(regex,initial_text)
special_words = []
mirror_words = []

for pair in filtered_words:
    word1 = pair.group("word1")
    word2 = pair.group("word2")

    if len(word1) >= 3 and len(word2) >= 3:
        special_words.append([word1, word2])

    mirrored_word1 = word1[::-1]
    if mirrored_word1 == word2:
        mirror_words.append([word1, word2])


pair_count = len(special_words)
for thing in mirror_words:
    if thing not in special_words:
        pair_count += 1

# print(special_words)
# print(mirror_words)
if pair_count > 0:
    print(f"{pair_count} word pairs found!")
else:
    print("No word pairs found!")

special_words2 = []
for double in mirror_words:
    special_words2.append(double[0])
    special_words2.append(double[1])

if len(special_words2) > 0:
    print(f"The mirror words are:")
    i = 0
    turns = len(special_words2)
    comma_needed = len(special_words2) - 2
    comma_count = 0
    while i < turns:
        print(f"{special_words2[i]} <=> {special_words2[i+1]}", end ="")
        if comma_count < comma_needed:
            print(f", ", end="")

        i += 2
        comma_count += 2

else:
    print(f"No mirror words!")

