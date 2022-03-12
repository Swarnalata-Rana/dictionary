dict= {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}
for key,values in list(dict.items()):
    word = ""
for i in key:
    if i != " ":
        word += i
print(word)
dict[word] = dict.pop(key)
print(dict)