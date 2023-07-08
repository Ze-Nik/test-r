def sorts(m):
    for i in range(1, len(m)):
        v = m[i]
        j = i
        while j > 0 and m[j - 1] > v:
            m[j] = m[j - 1]
            j = j - 1
        m[j] = v
def binp(m, l, h, n):
    mid = (l + h) // 2
    if m[mid] == n:
        return mid
    if l > h:
        return -1
    if m[mid] > n:
        return binp(m, l, mid - 1, n)
    else:
        return binp(m, mid + 1, h, n)


n = 2
m = [9, 15, 1, 28, 3, 62, 78, 2]
print(m)
sorts(m)
print(m)
i = binp(m, 0, len(m) - 1, n)
print(i)
