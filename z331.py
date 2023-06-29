from math import sqrt


def area(a, b, c):
    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    if s <= 0:
        return "такого треугольника не существует"
    return s


a, b, c = float(input()), float(input()), float(input())
print(area(a, b, c))
