list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
res={}
for key in list1:
    for value in list2:
        res[key]=value
        list2.remove(value)
        break
print(res)
