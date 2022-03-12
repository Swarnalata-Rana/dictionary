a=[20,10,3,24]
i=0
m={}
while i<len(a):
    s=""
    j=0
    d=str(a[i])
    while j<len(d):
        # print(d[j])
        if d[j]=="1":
            s=s+"one"
        if d[j]=="2":
            s=s+"two"
        if d[j]=="3":
            s=s+"three"
        if d[j]=="4":
            s=s+"four"
        if d[j]=="5":
            s=s+"five"
        if d[j]=="6":
            s=s+"six"
        if d[j]=="7":
            s=s+"seven"
        if d[j]=="8":
            s=s+"eight"
        if d[j]=="9":
            s=s+"nine"
        if d[j]=="0":
            s=s+"zero"
        j=j+1
    i=i+1
    m[d]=s
print(m)