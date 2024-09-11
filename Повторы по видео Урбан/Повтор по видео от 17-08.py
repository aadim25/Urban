# Полиморфизм
# Инкапсуляция
# Наследование
# Абстракция
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f'Сотрудник: {self.name}, Должность: {self.position}'

class Developer (Employee):
    def __init__(self, name, position, programming_language):
        # self.name = name
        # self.position = position
        # Employee.__init__(self, name, position)
        super().__init__(name, position)
        self.programming_language = programming_language

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info}, Язык программирования {self.programming_language}'

class Manager(Employee):
    def __init__(self, name, position, team_size):
        super().__init__(name, position)
        self.team_size = team_size

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info}, Размер команды {self.team_size}'

class RemoteWorker:
    def __init__(self, location):
        self.location = location

    def get_location(self):
        return f'Работает удаленно из {self.location}'

class RemoteDeveloper(Developer, RemoteWorker):
    def __init__(self, name,position, programming_language,location):
        super().__init__(name,position,programming_language,location)

# employee = Employee('Алиса', 'Менеджер')
developer = Developer('Саша', 'Разработчик','Python')
manager = Manager('Алиса','Менеджер', 20)
remote_developer = RemoteDeveloper('Давид','Сеньёр разработчик','Python','Латинская Америка')
# print(employee.get_info())
print(manager.get_info())
print(developer.get_info())
print(remote_developer.location)
print(RemoteDeveloper.__mro__)