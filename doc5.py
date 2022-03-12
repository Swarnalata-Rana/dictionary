d={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
s= dict(sorted(d.items()))
print('ascending order : ',s)
s1= dict(sorted(d.items(),reverse=True))
print('descending order : ',s1)
