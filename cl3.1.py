from random import randint

class Voin():
    health = 100
    bron = 100
    vin = 100

    def __init__(self, name):
        self.name = name

    def ydar(self, other):
        if self.vin <= 0:
            other.health -= randint(0, 10)
        else:
            other.health -= randint(10, 30)
            self.vin -= 10
        print("Ударил", self.name, 'У', other.name, 'осталось броня -', self.bron, 'здоровье -', self.health,
              'выносливость -', self.vin)

    def zach(self):
        if self.bron <= 0:
            self.health = randint(10, 30)
        else:
            self.health -= randint(0, 20)
            self.bron -= randint(0, 10)
        print(self.name, 'защищается,', 'броня -', self.bron, 'здоровье -', self.health,
              'выносливость -', self.vin)


v1 = Voin('Voin1')
v2 = Voin('Voin2')
while v1.health > 10 and v2.health > 10:
    r1 = randint(0, 1)
    r2 = randint(0, 1)
    if r1 == 0 and r2 == 0:
        pass
    if r1 == 1 and r2 == 0:
        v2.zach()
    if r1 == 0 and r2 == 1:
        v1.zach()
    if r1 == 1 and r2 == 1:
        v1.ydar(v2)
        v2.ydar(v1)

if v1.health <= 0:
    print("Победил ", v2.name)
    k = input("Добить проигравшего? ")
    if k == 'да':
        print(v1.name, 'убит')
    else:
        print('вы сохранили жизнь', v1.name)

else:
    print("Победил ", v1.name)
    k = input("Добить проигравшего? ")
    if k == 'да':
        print(v2.name, 'убит')
    else:
        print('вы сохранили жизнь', v2.name)
