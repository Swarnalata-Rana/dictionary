dic={3:87,9:87}
n=int(input("enter the no:-"))
if not dic:
    print("yes empty")
else:
    ("not empty")



d={"a":2,"b":4}
d1={"d":6,"e":8}
for i in (d,d1):
    d.update(d1)
print(d)
a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
m={}
for i in a.values():
    c=len(i)
    m[i]=c
print(m)



dict={"a":20,"b":23.5,"c":40,"d":40.1}
m={}
max=0
key=0
for i in dict:
    if dict[i]>max:
        max=dict[i]
        m.update({"d":max})
print(m)
