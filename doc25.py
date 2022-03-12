list = [1, 2, 3, 4]
dict = current = {}
for i in list:
    current[i] = {}
    current = current[i]
print(dict)
# doc=28