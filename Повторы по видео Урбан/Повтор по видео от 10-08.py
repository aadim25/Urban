# Повтор лекции по видео от 10-08-24
# Полиморфизм
# Инкапсуляция
# Наследование
# Абстракция

class Dog:
    # name = 'Хаски'
    # bread = 'Супер порода'
    # age = 10
    bread = 'Colosus Impers'

    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def __add__(self, other):
        if isinstance(other, Dog):
            self.name += other.name
            self.color += other.color
        else:
            self.age += other
        return self

    def __eq__(self, other):
        return self.age == other.age

haski = Dog('Хаски', 'Белый', 10)
richie = Dog('Ричи','Оранжевый', 15)
mopsa = Dog('Мопс','Черный', 5)
print(haski+mopsa)
print(haski.name)
print(haski.color)
mopsa.age+=5
# print(haski.__add__(10))
# print(haski + 10)
# print (haski.name)
print (haski.age)
print (haski == mopsa)
# print (haski.color)
# print()
# print(richie.name)
# print(richie.age)
# print(richie.color)


# class Employee:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#
#     def get_info(self):
#         print('3')
#         return f'Сотрудник: {self.name}, Должность: {self.position}'
#
# class Developer (Employee):
#     def __init__(self, name, position, programming_language):
#         # self.name = name
#         # self.position = position
#         # Employee.__init__(self, name, position)
#         super().__init__(name, position)
#         self.programming_language = programming_language
#
#     def get_info(self):
#         print('2')
#         base_info = super().get_info()
#         return f'{base_info}, Язык программирования {self.programming_language}'
#
# class Manager(Employee):
#     def __init__(self, name, position, team_size):
#         super().__init__(name, position)
#         self.team_size = team_size
#
#     def get_info(self):
#         base_info = super().get_info()
#         return f'{base_info}, Размер команды {self.team_size}'
#
# class RemoteWorker:
#     def __init__(self, location):
#
#         self.location = location
#
#     def get_location(self):
#         print('4')
#         return f'Работает удаленно из {self.location}'
#
# class RemoteDeveloper(Developer, RemoteWorker):
#     def __init__(self, name, position, programming_language, location):
#         # super().__init__(name, position, programming_language, location)
#         # Developer.__init__(self, name, position, programming_language)
#         # RemoteWorker.__init__(self, location)
#         super(Employee, self).__init__(location)
#     def get_info(self):
#         print ('1')
#         dev_info = super().get_info()
#         location_info = self.get_location()
#         return f'{dev_info}, {location_info}'
#
# # employee = Employee('Алиса', 'Менеджер')
# # developer = Developer('Саша', 'Разработчик','Python')
# # manager = Manager('Алиса','Менеджер', 20)
# remote_developer = RemoteDeveloper('Давид','Сеньёр разработчик','Python','Латинская Америка')
# # print(employee.get_info())
# # print(manager.get_info())
# # print(developer.get_info())
# print(remote_developer.get_info())
# # print(RemoteDeveloper.__mro__)