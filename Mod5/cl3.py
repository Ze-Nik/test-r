from random import randint

class Voin():
    health = 100

    def __init__(self, name):
        self.name = name

    def ydar(self, other):
        other.health -= 20
        print("Ударил", self.name, 'У', other.name, 'осталось здоровья', other.health)

v1 = Voin('Voin1')
v2 = Voin('Voin2')
while v1.health > 0 and v2.health > 0:
    r = randint(0, 1)
    if r == 0:
        v1.ydar(v2)
    else:
        v2.ydar(v1)
if v1.health <= 0:
    print("Победил ", v2.name)
else:
    print("Победил ", v1.name)
