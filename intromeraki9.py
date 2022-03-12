str1 = 'MISSISSIPPI' 
dict = {}
for letter in str1:
    dict[letter] = dict.get(letter, 0) + 1
print(dict)
# m=9
  

