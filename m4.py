def sort(m):
    if len(m) > 1:
        mid = len(m) // 2
        l = m[:mid]
        r = m[mid:]
        sort(l)
        sort(r)
        i, j, k = 0, 0, 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                m[k] = l[i]
                i += 1
            else:
                m[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            m[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            m[k] = r[j]
            j += 1
            k += 1


def binp(m, l, h, n):
    mid = (l + h) // 2
    print(mid)
    if m[mid] == n:
        return mid
    if m[mid] > n:
        return binp(m, l, mid - 1, n)
    else:
        return binp(m, mid + 1, h, n)


n = 44
m = [1, 3, 7, 15, 26, 27, 30, 32, 45]
print(m)
sort(m)
print(m)
i = binp(m, 0, len(m) - 1, n)
print(i)
