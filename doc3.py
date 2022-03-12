dict={"a":20,"b":23.5,"c":40,"d":40.1}
m={}
max=0
key=0
for i in dict:
    if dict[i]>max:
        max=dict[i]
        m.update({"d":max})
print(m)
