'''
Задача "История строительства":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".

В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.

Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к
 атрибутам класса используя ссылку на сам класс - cls.
Дополните метод __new__ так, чтобы:
Название объекта добавлялось в список cls.houses_history.
Название строения можно взять из args по индексу.
'''
class House:
    houses_history = []
    __instance = None
    def __new__(cls, *args):
        global houses_history
        # print (args)
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        House.houses_history.append(args[0])
            # print (len(args))
            # print (len(House.houses_history))
        return cls.__instance
    def __init__(self, name, number_of_floors):
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

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
print (f'{h2.name} снесён, но он останется в истории')
print (f'{h3.name} снесён, но он останется в истории')


# Удаление объектов
del h2
del h3

print(House.houses_history)
print (f'{h1.name} снесён, но он останется в истории')
