d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}
m = d.items()
m = list(m)
k = 0
s = []
so = []
l = {}
for i in range(len(m)):
    n = list(m[i])
    s.append(n[0])
    so.append(n[1])
l = dict(zip(so, s))
print(l)





