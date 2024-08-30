class House:
    def __init__(self, name:str, number_of_floors:int):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return self.name
    def go_to (self, new_floors:int):
        if new_floors > self.number_of_floors:
            print ("Такого этажа не существует")
        else:
            for i in range(1,new_floors+1):
                print (i)
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors==other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other

    def __add__(self, other):
        if isinstance(other, House):
            self.number_of_floors += other.number_of_floors
            return self
        elif isinstance(other, int):
            self.number_of_floors += other
            return self

    def __radd__(self, other):
        # написанная ниже строка дана Юрой, но я пока плохо в этом ориентируюсь
        return self.__add__(other)
        # закоментированный код был изначально написан по статьям из интернета
        # if isinstance(other, House):
        #     self.number_of_floors += other.number_of_floors
        #     return self
        # elif isinstance(other, int):
        #     self.number_of_floors += other
        #     return self

    def __iadd__(self, other:int):
        # написанная ниже строка дана Юрой, но я пока плохо в этом ориентируюсь
        return self.__add__(other)
        # закоментированный код был изначально написан по статьям из интернета
        # if isinstance(other, House):
        #     self.number_of_floors += other.number_of_floors
        #     return self
        # elif isinstance(other, int):
        #     self.number_of_floors += other
        #     return self

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(f'Название: {h1.__str__()}, кол-во этажей: {h1.__len__()}.')
print(f'Название: {h2.__str__()}, кол-во этажей: {h2.__len__()}.')

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(f'Название: {h1.__str__()}, кол-во этажей: {h1.__len__()}.')

print(h1 == h2)

h1 += 10  # __iadd__
h2 = 10 + h2  # __radd__

print(f'Название: {h1.__str__()}, кол-во этажей: {h1.__len__()}.')
print(f'Название: {h2.__str__()}, кол-во этажей: {h2.__len__()}.')

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__


