
dict= {'a': 100, 'b':200, 'c':300}
sum=0
for i in dict.values():
    sum=sum+i
print(sum)
# doc=13

# other type
dict = {'a': 100, 'b':200, 'c':300}
sum=0
for i in dict:
    sum=sum+dict[i]
print(sum)