#\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b


import re

text = input()

# matches = re.findall(r"\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b", text)
# matches = re.findall(r"\+359([ -])2\1\d{3}\1\d{4}\b", text)
#s grupi ne stava findall, zashtoto printira vutreshnite grupi

matches = re.finditer(r"\+359([ -])2\1\d{3}\1\d{4}\b", text)

# print(", ".join(matches))
#search vrushta 1 otrkivane, matches.group()

output = list()
for match in matches:
    output.append(match.group())

print(", ".join(output))