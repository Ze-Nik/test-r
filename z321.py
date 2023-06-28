sp = [1, 4, 1, 6, "hello", "a", 5, "hello"]
k = 0
spp = []
for i in range(len(sp)):
    for j in range(len(sp)):
        if sp[i] == sp[j]:
            k += 1
    if k > 1:
        spp.append(sp[i])
    k = 0
print(set(spp)
