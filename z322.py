from random import randint

max = 0
n = 5
m = [[randint(0, 100) for i in range(n)] for j in range(n)]
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] > max:
            max = m[i][j]
print(max)
print(m)
