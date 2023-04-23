x, y, p = int(input()), int(input()), float(input())
i = 0
p = (p / 100) + 1
while x < y:
    x = x * p
    x = int(x)
    i += 1
print(i)


