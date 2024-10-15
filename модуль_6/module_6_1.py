class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

class Plant:

    def __init__(self,name):
        self.name = name
        self.edible = False
class Mammal (Animal):
    def __init__(self, name, food):
        self.name = name
        self.food = food
    def eat(self,food):
        if food.adible:
            print(f"{self.name} съел {food.name}")
class Predator (Animal):
    def __init__(self, name, alive):
        self.name = name
        super().alive = alive
    def eat(self, food):
        if food:
            print (f"{self.name} съел {food.name}")


class Flower (Plant):
    def __init__(self, name):
        self.name = name


class Fruit (Plant):
    edible = True
    def __init__(self, name):
        self.name = name

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

