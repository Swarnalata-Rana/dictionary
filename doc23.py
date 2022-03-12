list=[20,10,3,24]
list1=['twozero','onezero','three','twofour']
i=0
d={}
while i<len(list):
    j=0
    while j<len(list1):
        if i==j:
            d[list[i]]=list1[j]
        j=j+1
    i=i+1
print(d)