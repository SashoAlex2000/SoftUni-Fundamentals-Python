import re

text = input()

# matches = re.findall(r"\b[A-Z][a-z]+\b \b[A-Z][a-z]+\b", text)
matches = re.findall(r"\b[A-Z][a-z]+\b \b[A-Z][a-z]+\b", text)


print(" ".join(matches))
#search vrushta 1 otrkivane, matches.group()
#scobite grupirat elementi