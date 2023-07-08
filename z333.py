m = [52, 9, 11, 2, 56]
k1 = 0
k2 = 0
ch = ''
for i in range(len(m) - 1):
    for j in range(len(m) - i - 1):
        k1 = len(str(m[j]))
        if k1 == 1:
            d1 = 1
        else:
            d1 = 10 * (k1 - 1)
        k2 = len(str(m[j + 1]))
        if k2 == 1:
            d2 = 1
        else:
            d2 = 10 * (k2 - 1)
        if (int(m[j]) // d1) < (int(m[j + 1]) // d2):
            m[j], m[j + 1] = m[j + 1], m[j]
for i in range(len(m)):
    ch = ch + str(m[i])
print(ch)


