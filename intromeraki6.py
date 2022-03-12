dic1={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
l=[]
a=dict()
for key,val in dic1.items():
    if val not in a:
        l.append(val)
        a[key]=val
print(a)