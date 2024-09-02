class Human:

    head = True
    def __init__(self, name,age):
        self.name = name
        self.age = age
        # self.say_info()

den = Human('Денис', 22)
max = Human('Максим',22)
a = 6
print(f'Привет, меня зовут {den.name}, мне {den.age} года')
print(f'Привет, меня зовут {max.name}, мне {max.age} года')
print(Human.head)
