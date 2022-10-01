initial_text = list(input())
emoticon_list = []


# for word in initial_text:
#     if ":" in word:
#         emoticon_list.append(word)
#
# for emoticon in emoticon_list:
#     if "." in emoticon:
#         emoticon.replace(".", "")
#     print(emoticon)


for i in range(len(initial_text)):
    if initial_text[i] == ":":
        emoticon_to_add = initial_text[i] + initial_text[i+1]
        emoticon_list.append(emoticon_to_add)
#
# for ccc in emoticon_list:
#     print(ccc)
    
print("\n".join(emoticon_list))